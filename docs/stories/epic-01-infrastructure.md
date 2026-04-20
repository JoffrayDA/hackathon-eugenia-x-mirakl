# Epic 01 — Infrastructure & Données Mock

**Priorité : CRITIQUE — À faire en premier (Jour 1 matin)**

---

## Story 1.1 — Setup projet Backend
**Estimation : 30min**

Setup FastAPI avec :
- Structure de dossiers (`agents/`, `tools/`, `data/`, `api/`)
- Pydantic models : `Ticket`, `Order`, `Customer`, `AgentEvent`, `HumanValidation`
- Configuration OpenAI client
- CORS pour le frontend Next.js
- Endpoint healthcheck GET /health

**Critère d'acceptance** : `uvicorn main:app` démarre sans erreur

---

## Story 1.2 — Données mock
**Estimation : 45min**

Créer les fichiers JSON dans `src/data/mock/` :

`orders.json` — 20 commandes couvrant tous les statuts :
- 4 non expédiées (dont 2 dépassant le SLA)
- 4 expédiées (dont 2 "perdues" par le transporteur mock)
- 4 livrées avec problème (défaut, mauvais article)
- 4 en cours d'annulation
- 4 avec demande de retour

`customers.json` — 10 clients (2 VIP avec > 5 commandes)

`merchant.json` — 1 marchand avec :
- Politique retour : 30 jours
- SLA expédition : 48h
- Seuil remboursement auto : 0€ (tout passe par humain)

`carrier_mock.json` — Réponses simulées GLS/Colissimo/DHL

`scenarios.json` — 10 tickets pré-écrits pour la démo (1 par case SAV + variantes)

**Critère d'acceptance** : Tous les fichiers valides JSON, chargés au démarrage sans erreur

---

## Story 1.3 — Setup projet Frontend
**Estimation : 30min**

Setup Next.js 14 avec :
- App Router, TypeScript, Tailwind CSS
- Structure : `app/`, `components/`, `lib/`, `types/`
- Types TypeScript alignés avec les Pydantic models backend
- Client HTTP (`lib/api.ts`) avec fetch vers le backend
- Client SSE (`lib/stream.ts`) pour le flux temps réel

**Critère d'acceptance** : `npm run dev` démarre, page blanche sans erreur console

---

## Story 1.4 — Endpoint SSE (Server-Sent Events)
**Estimation : 30min**

`GET /stream` — endpoint SSE qui :
- Maintient une connexion ouverte par client
- Pousse les `AgentEvent` au fil de l'eau
- Gère la déconnexion proprement
- Broadcast à tous les clients connectés (file globale en mémoire)

`POST /events/emit` — endpoint interne appelé par les agents pour pusher un event

**Critère d'acceptance** : Ouvrir `GET /stream` dans curl → recevoir des events data: JSON toutes les X secondes
