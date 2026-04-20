# Epic 03 — API Backend

**Priorité : HAUTE — Colle agents + frontend (Jour 1 fin d'après-midi)**

---

## Story 3.1 — Endpoints Tickets
**Estimation : 45min**

```
POST /tickets/ingest
  Body: { customer_message: str, order_id: str }
  → Lance orchestrateur en background task
  → Retourne immédiatement { ticket_id, status: "processing" }

GET /tickets
  Query: status?, type?, limit?
  → Liste paginée des tickets

GET /tickets/{ticket_id}
  → Ticket complet avec tous les AgentEvents
```

**Critère d'acceptance** : POST /ingest → ticket créé + agents lancés en async + visible GET /tickets

---

## Story 3.2 — Endpoints Validations Humaines
**Estimation : 30min**

```
GET /validations
  Query: status=pending
  → Liste des validations en attente

GET /validations/{validation_id}
  → Validation avec contexte complet

POST /validations/{validation_id}/approve
  Body: { approved_amount?: float }
  → Déclenche l'action (remboursement mock)
  → Émet AgentEvent "human_approved"

POST /validations/{validation_id}/reject
  Body: { reason: str }
  → Notifie l'agent
  → Émet AgentEvent "human_rejected"
```

**Critère d'acceptance** : Créer validation → GET /validations → POST /approve → event SSE "approved" reçu

---

## Story 3.3 — Endpoint Override
**Estimation : 30min**

```
POST /tickets/{ticket_id}/override
  Body: { action: "pause" | "take_over" | "resume", note?: str }
  → Pause ou reprend les agents sur ce ticket
  → Émet AgentEvent "human_override"

GET /tickets/{ticket_id}/events
  → Stream SSE des events d'un ticket spécifique
```

**Critère d'acceptance** : POST /override pause → agents s'arrêtent, event override visible dashboard

---

## Story 3.4 — Endpoint Scénarios Démo
**Estimation : 20min**

```
POST /demo/load-scenario/{scenario_id}
  → Charge un scénario mock pré-défini
  → Crée les commandes/clients/tickets correspondants
  → Optionnel: auto-lance les agents

POST /demo/reset
  → Remet l'état à zéro (pour les démos successives)

GET /demo/scenarios
  → Liste des scénarios disponibles
```

**Critère d'acceptance** : Pendant la démo, lancer un scénario en 1 appel API reproductible
