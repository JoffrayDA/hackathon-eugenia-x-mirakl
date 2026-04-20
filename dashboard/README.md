# Dashboard Marchand

Interface de pilotage SAV en temps réel.

## Stack
- Next.js 14 + TypeScript + Tailwind CSS
- Connexion SSE vers n8n pour le flux live

## Vues
- **Flux Live** — timeline des actions agents en temps réel
- **File SAV** — tous les tickets avec statut
- **Validations** — remboursements en attente d'approbation
- **Détail Ticket** — audit trail complet + reasoning des agents

## Lancement
```bash
npm install
cp ../.env.example .env.local
npm run dev
```
