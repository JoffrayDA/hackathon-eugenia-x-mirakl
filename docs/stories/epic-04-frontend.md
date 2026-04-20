# Epic 04 — Frontend Dashboard

**Priorité : HAUTE — UX est un livrable (Jour 2 matin)**

---

## Story 4.1 — Layout + Navigation
**Estimation : 30min**

Composant `AppShell` avec :
- Header : logo Eugenia, nom marchand, indicateur agents actifs (count pulsant)
- Navigation : [Flux Live] [File SAV] [Validations] [Stats]
- Badge rouge sur [Validations] si items en attente
- Responsive mobile (pour démo sur téléphone si besoin)

**Critère d'acceptance** : Navigation entre les 4 vues sans rechargement

---

## Story 4.2 — Vue Flux Live
**Estimation : 1h30**

Composants :
- `LiveFeed` : conteneur qui écoute le SSE (`/stream`)
- `AgentEventCard` : carte unitaire avec agent, action, reasoning, timestamp relatif
  - Variant `validation` : fond orange/rouge, CTA "Valider maintenant"
  - Variant `resolved` : fond vert léger
  - Variant `in_progress` : spinner bleu
- Animation : slide-down + fade-in à chaque nouvel event
- Bouton [Pause] pour arrêter le défilement (utile pendant la démo)
- Panel latéral : clic sur une carte → `TicketDetailPanel` (Story 4.5)

**Critère d'acceptance** : POST /ingest → card apparaît en < 2s dans le flux, en live

---

## Story 4.3 — Vue File SAV
**Estimation : 45min**

Composants :
- `TicketTable` : tableau avec colonnes #, Client, Type, Statut, Dernière MAJ
- `TicketStatusBadge` : chip coloré selon statut (voir UX spec couleurs)
- `TicketTypeIcon` : icône emoji selon type SAV
- Filtres : tabs [Tous] [En cours] [Résolus] [Escaladés]
- Tri par date (défaut: plus récent)
- Clic sur ligne → `TicketDetailPanel`

**Critère d'acceptance** : Tous les tickets mockés affichés, filtres fonctionnels, clic ouvre le détail

---

## Story 4.4 — Vue Validations Humaines
**Estimation : 1h**

Composants :
- `ValidationInbox` : liste des validations en attente
- `ValidationCard` : carte complète avec :
  - Montant en gras
  - Contexte rapide (3-4 bullets: date commande, historique client, pièces jointes, politique)
  - Citation de l'agent (son raisonnement)
  - Boutons : [✅ Approuver] [❌ Rejeter] [✏️ Modifier montant]
- Modal de rejet : champ "Raison" obligatoire
- Modal de modification : input montant avec validation
- Feedback optimiste : card disparaît immédiatement après action + toast

**Critère d'acceptance** : Validation en attente → approuver → card disparaît → event SSE "approved" dans flux live

---

## Story 4.5 — Panel Détail Ticket
**Estimation : 1h**

Composant `TicketDetailPanel` (slide-in depuis la droite) :
- Header : numéro ticket, client, commande, statut
- Section "Message client" : verbatim en card
- Section "Audit Trail" : timeline chronologique de tous les AgentEvents
  - Chaque event : timestamp, nom agent, action, reasoning expandable
  - Expand "Voir le raisonnement" → détail de ce que l'agent a consulté
- Section "Message prêt à envoyer" : prévisualisation avec [Envoyer] [Modifier]
- Footer : [Mettre en pause les agents] [Prendre en charge manuellement]

**Critère d'acceptance** : Audit trail complet visible, reasoning expandable, override fonctionnel

---

## Story 4.6 — Vue Stats (optionnel si temps)
**Estimation : 30min**

Métriques simples :
- Taux résolution autonome (gauge)
- Temps moyen traitement (chiffre)
- Répartition par type SAV (donut)
- Nombre de validations humaines traitées

Utiliser `recharts` ou simple CSS pour les graphiques.

**Critère d'acceptance** : Page affiche des chiffres cohérents avec l'état des tickets
