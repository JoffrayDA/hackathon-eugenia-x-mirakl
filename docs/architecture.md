# Architecture Technique — Eugenia

## Vue d'ensemble

```
┌─────────────────────────────────────────────────────────────┐
│                      FRONTEND (Next.js)                      │
│  Dashboard Marchand — Vue Flux / File / Validation / Détail  │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP + SSE (Server-Sent Events)
┌──────────────────────────▼──────────────────────────────────┐
│                    BACKEND (FastAPI Python)                   │
│                                                              │
│  POST /tickets/ingest    GET /tickets        GET /stream     │
│  POST /tickets/{id}/override                                  │
│  POST /validations/{id}/approve|reject                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    ORCHESTRATOR AGENT                         │
│              (GPT-4o + function calling)                     │
│   Reçoit ticket → classe → route vers agent spécialisé      │
└────┬──────────┬──────────┬──────────┬──────────┬────────────┘
     │          │          │          │          │
┌────▼─┐  ┌────▼─┐  ┌────▼─┐  ┌────▼─┐  ┌────▼──┐
│Ship. │  │Deliv.│  │Defect│  │Cancel│  │Return │
│Agent │  │Agent │  │Agent │  │Agent │  │Agent  │
└────┬─┘  └────┬─┘  └────┬─┘  └────┬─┘  └────┬──┘
     └──────────┴──────────┴─────────┴──────────┘
                           │
                    ┌──────▼──────┐
                    │   TOOLS      │
                    │ (Mock APIs)  │
                    │             │
                    │ - OrderDB   │
                    │ - CarrierAPI│
                    │ - PolicyDB  │
                    │ - EmailSend │
                    │ - ReturnGen │
                    └─────────────┘
```

## Stack Technique

| Composant | Technologie | Justification |
|---|---|---|
| Backend | Python 3.11 + FastAPI | Rapide à coder, async natif, parfait pour agents |
| LLM | OpenAI GPT-4o | Function calling robuste, context long |
| Agent Framework | OpenAI Agents SDK (ou implémentation custom légère) | Contrôle total, pas de magie noire |
| Frontend | Next.js 14 + TypeScript + Tailwind | App Router, SSE natif, UI rapide |
| Real-time | Server-Sent Events (SSE) | Simple, unidirectionnel, pas besoin de WS |
| Data | JSON files + in-memory (SQLite optionnel) | Zéro infra, démo agile |
| State | Zustand (frontend) | Léger, réactif |

## Structure de données

### Ticket
```typescript
interface Ticket {
  id: string
  created_at: string
  customer: Customer
  order: Order
  type: 'unshipped' | 'not_received' | 'defective' | 'cancellation' | 'return'
  raw_message: string
  status: 'pending' | 'in_progress' | 'resolved' | 'escalated' | 'awaiting_human'
  confidence_score: number      // 0-100, si < 70 → escalade
  agent_events: AgentEvent[]    // audit trail complet
  resolution?: Resolution
  human_validation?: HumanValidation
}
```

### AgentEvent (le coeur de la transparence)
```typescript
interface AgentEvent {
  id: string
  timestamp: string
  agent: string                  // 'orchestrator' | 'shipping' | etc.
  action: string                 // 'classified_ticket' | 'checked_carrier' | etc.
  reasoning: string              // Explication en langage naturel pour le marchand
  data?: Record<string, any>     // Données consultées/produites
  requires_human: boolean
}
```

### Order (mock)
```typescript
interface Order {
  id: string
  status: 'pending' | 'processing' | 'shipped' | 'delivered' | 'cancelled'
  items: OrderItem[]
  shipping: ShippingInfo
  merchant_id: string
  customer_id: string
  total_amount: number
  created_at: string
  sla_deadline: string
}
```

## Architecture Agents

### Pattern : Agent avec Tools

Chaque agent spécialisé reçoit :
1. Le ticket complet
2. L'historique commande
3. Les politiques du marchand
4. Les actions déjà effectuées

Et dispose de tools (function calling) :
```python
# Exemple ShippingAgent tools
tools = [
    check_carrier_status,      # → statut transporteur mock
    get_merchant_sla,          # → délais contractuels
    send_customer_notification, # → email mock
    request_carrier_relay,     # → relance transporteur
    escalate_to_human,         # → crée validation humaine
    emit_agent_event,          # → log dashboard temps réel
]
```

### Orchestrateur

```python
# Prompt système orchestrateur
ORCHESTRATOR_SYSTEM = """
Tu es l'orchestrateur SAV d'Eugenia. Tu reçois des tickets clients et tu dois :
1. Classifier précisément le type de problème (score de confiance obligatoire)
2. Router vers l'agent spécialisé approprié
3. Si confiance < 70%, escalader immédiatement à un humain avec explication

Règles absolues :
- Tu ne déclenches JAMAIS de remboursement directement
- Tu loggues CHAQUE décision avec une explication en français simple
- En cas de doute, tu escalades
"""
```

### Flux d'exécution

```
Ticket entrant
    │
    ▼
Orchestrator (classify + route)
    │
    ├─ confidence < 70% ──→ EscaladeAgent → HumanValidationQueue
    │
    └─ confidence ≥ 70% ──→ Agent Spécialisé
                                │
                                ├─ Consulte tools (order, carrier, policy)
                                ├─ Émet AgentEvents (SSE → dashboard)
                                ├─ Prend décision
                                │
                                ├─ Décision = remboursement ──→ HumanValidationQueue
                                └─ Décision = action ──→ Exécute + Notifie client
```

## Données Mock

Fichiers JSON dans `src/data/mock/` :
- `orders.json` — 20 commandes variées (tous statuts)
- `customers.json` — 10 clients (dont 2 VIP)
- `merchants.json` — 1 marchand avec politiques SAV complètes
- `carrier_responses.json` — réponses simulées transporteur
- `tickets_scenarios.json` — 10 tickets couvrant tous les cas UC1

## Sécurité & Guardrails

- Validation Pydantic sur tous les inputs
- Liste blanche des actions autorisées par agent
- `requires_human: true` sur toute décision financière → bloque l'exécution jusqu'à approval
- Logging complet de tous les appels LLM (tokens, latence, coût estimé)
