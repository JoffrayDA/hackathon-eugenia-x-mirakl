# Backend — Webhooks & API

Pont entre n8n et le dashboard. Expose les endpoints nécessaires.

## Endpoints

```
POST /webhook/ticket        ← reçoit les tickets (appelé par n8n)
GET  /tickets               → liste des tickets
GET  /tickets/:id           → détail + audit trail
POST /validations/:id/approve
POST /validations/:id/reject
GET  /stream                → SSE flux live dashboard
POST /demo/scenario/:id     → charge un scénario démo
POST /demo/reset            → remet à zéro
```

## Lancement
```bash
pip install -r requirements.txt
cp ../.env.example .env
uvicorn main:app --reload
```
