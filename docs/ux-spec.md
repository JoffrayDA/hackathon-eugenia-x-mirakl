# Spec UX — Dashboard Marchand Eugenia

## Principes de Design

1. **Transparence radicale** : le marchand comprend TOUJOURS ce que fait l'agent, sans être développeur
2. **Confiance progressive** : les agents prouvent leur pertinence avant que le marchand leur délègue plus
3. **Reprise de main immédiate** : 1 clic pour stopper/overrider n'importe quelle action
4. **Densité utile** : beaucoup d'info, mais hiérarchisée — rien d'inutile à l'écran

---

## Layout Principal

```
┌─────────────────────────────────────────────────────────────────┐
│  🟢 Eugenia  [Flux Live]  [File SAV]  [Validations ⚠️ 2]  [Stats] │
│  Marchand : Boutique Demo              ○ 3 agents actifs         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [VUE PRINCIPALE — change selon onglet sélectionné]             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Vue 1 — Flux Live (page d'accueil)

**Concept** : une timeline en temps réel des actions des agents, lisible comme un fil d'actualité.

```
┌─────────────────────────────────────────────────────────────────┐
│  FLUX EN DIRECT                              ● Live    [Pause]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─ il y a 2s ──────────────────────────────────────────────┐  │
│  │  🤖 Agent Livraison  •  Ticket #1042                      │  │
│  │  ✅ Colis localisé chez le transporteur                   │  │
│  │  "Le colis GLS#8823 est en transit — livraison prévue     │  │
│  │   demain avant 18h. J'ai notifié le client."              │  │
│  │  [Voir le ticket]  [Voir le message envoyé]               │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌─ il y a 45s ─────────────────────────────────────────────┐  │
│  │  🤖 Agent Orchestrateur  •  Ticket #1041                  │  │
│  │  📋 Nouveau ticket classifié : Produit défectueux         │  │
│  │  "Confiance : 94%. Routé vers Agent Défauts."             │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌─ il y a 2min ────────────────────────────────────────────┐  │
│  │  ⚠️ Agent Défauts  •  Ticket #1039                        │  │
│  │  🔴 VALIDATION REQUISE — Remboursement 89,90€             │  │
│  │  "Produit manifestement défectueux à réception.           │  │
│  │   Je recommande le remboursement complet."                │  │
│  │  [→ Valider maintenant]                                   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Comportement** :
- Nouveau event → carte apparaît en haut avec animation slide-down
- Les cards de validation humaine sont en rouge/orange, sticky en haut
- Clic sur "Voir le ticket" → panel latéral droit avec détail complet
- Bouton [Override Agent] visible au hover sur chaque card

---

## Vue 2 — File SAV

**Concept** : kanban/liste de tous les tickets avec filtres rapides.

```
┌─────────────────────────────────────────────────────────────────┐
│  FILE SAV   [Tous 14]  [En cours 5]  [Résolus 7]  [Escaladés 2] │
│  🔍 Recherche...                          [+ Nouveau ticket]     │
├──────────┬──────────────────┬──────────┬──────────┬─────────────┤
│ #        │ Client           │ Type     │ Statut   │ Dernière MAJ│
├──────────┼──────────────────┼──────────┼──────────┼─────────────┤
│ #1042    │ Marie D.         │ 📦 Livr. │ ✅ Résolu│ il y a 2s  │
│ #1041    │ Jean-Paul M.     │ 🔧 Défaut│ ⚙️ Cours │ il y a 45s │
│ #1039    │ Sophie L.        │ 🔧 Défaut│ ⚠️ Attente│ il y a 2m  │
│ #1038    │ Thomas B.        │ ↩️ Retour│ ✅ Résolu│ il y a 8m  │
└──────────┴──────────────────┴──────────┴──────────┴─────────────┘
```

**Statuts visuels** :
- ⚙️ En cours → spinner gris
- ✅ Résolu → vert
- ⚠️ Attente validation → orange pulsant
- 🔴 Escaladé → rouge
- ⏸️ Overridé par humain → violet

---

## Vue 3 — Validations Humaines

**Concept** : inbox de décisions en attente. L'objectif est de permettre une validation en < 10 secondes.

```
┌─────────────────────────────────────────────────────────────────┐
│  2 DÉCISIONS EN ATTENTE                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🔴 Remboursement  •  Ticket #1039  •  Sophie L.         │   │
│  │  ────────────────────────────────────────────────────    │   │
│  │  Montant : 89,90€                                        │   │
│  │  Raison : Produit défectueux signalé à réception         │   │
│  │                                                          │   │
│  │  📋 Contexte rapide :                                    │   │
│  │  • Commande passée il y a 8 jours                        │   │
│  │  • 1ère commande de ce client                            │   │
│  │  • Photo fournie : oui (appareille visible)              │   │
│  │  • Politique retour : 30 jours ✓                         │   │
│  │                                                          │   │
│  │  🤖 L'agent dit : "Défaut clairement visible sur photo,  │   │
│  │  confiance 91%. Remboursement conforme à la politique."  │   │
│  │                                                          │   │
│  │  [Voir le ticket complet]                                │   │
│  │                                                          │   │
│  │  [✅ Approuver 89,90€]    [❌ Rejeter]    [✏️ Modifier]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Comportement** :
- [Rejeter] → modal avec champ "Raison du refus" (obligatoire, pour que l'agent apprenne)
- [Modifier] → permet d'ajuster le montant avant d'approuver
- Badge rouge sur l'onglet nav si validation en attente > 1h

---

## Vue 4 — Ticket Détail (Panel latéral)

**Concept** : audit trail complet d'un ticket, comme une fiche d'intervention.

```
┌─────────────────────────────────────────┐
│  Ticket #1041 — Produit défectueux  [×] │
│  Jean-Paul M. — Commande #CMD-8821      │
├─────────────────────────────────────────┤
│                                         │
│  MESSAGE CLIENT                         │
│  ┌───────────────────────────────────┐  │
│  │ "Bonjour, j'ai reçu mon article   │  │
│  │  hier mais il est cassé dans la   │  │
│  │  boîte. Photo ci-jointe."         │  │
│  └───────────────────────────────────┘  │
│                                         │
│  ACTIONS DES AGENTS ──────────────────  │
│                                         │
│  14:32:01  🤖 Orchestrateur             │
│  Classifié : Produit défectueux (94%)   │
│  Routé → Agent Défauts                  │
│  ▼ Voir le raisonnement                 │
│                                         │
│  14:32:04  🤖 Agent Défauts             │
│  Consulté : politique retour marchand   │
│  → Retours acceptés 30j ✓              │
│                                         │
│  14:32:07  🤖 Agent Défauts             │
│  Consulté : historique client           │
│  → 1ère commande, client standard       │
│                                         │
│  14:32:09  ⏳ EN ATTENTE VALIDATION     │
│  Décision : Remboursement 89,90€        │
│  [→ Aller valider]                      │
│                                         │
│  MESSAGE PRÊT À ENVOYER ─────────────   │
│  ┌───────────────────────────────────┐  │
│  │ "Bonjour Jean-Paul, nous avons    │  │
│  │  bien reçu votre signalement..."  │  │
│  └───────────────────────────────────┘  │
│  [Envoyer]  [Modifier]                  │
│                                         │
│  ─────────────────────────────────────  │
│  [⏸️ Mettre en pause les agents]        │
│  [👤 Prendre en charge manuellement]    │
└─────────────────────────────────────────┘
```

---

## Design System

### Couleurs
- `--green-500` : résolu, validé, confiant
- `--orange-400` : en attente humain, attention
- `--red-500` : escaladé, urgent, remboursement
- `--blue-500` : agent en cours d'action
- `--gray-100` : background cards
- `--purple-400` : action humaine effectuée

### Composants clés
- `AgentEventCard` : l'unité de base du flux live
- `ValidationCard` : card de validation humaine (rouge/orange)
- `TicketRow` : ligne de la file SAV
- `AuditTrail` : liste chronologique des AgentEvents
- `AgentBadge` : chip avec nom + icône de l'agent

### Iconographie agents
- 🤖 Orchestrateur
- 📦 Agent Livraison / Expédition
- 🔧 Agent Défauts
- ↩️ Agent Retours
- ❌ Agent Annulations

---

## Flux démo jury (golden path)

1. Ouvrir dashboard → montrer flux live avec 2-3 tickets en cours
2. Nouveau ticket entrant → classifier en live devant le jury
3. Agent résout autonomement → notification client générée
4. 2ème ticket → agent demande validation remboursement → jury valide
5. Override manuel d'un ticket → montrer la reprise de main
6. Stats finales : "8/10 tickets résolus sans intervention humaine"
