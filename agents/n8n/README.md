# n8n Workflows

## Import

1. Ouvrir n8n
2. Menu → Import workflow
3. Sélectionner le fichier JSON du dossier `workflows/`

## Workflows

| Fichier | Description |
|---|---|
| `orchestrator.json` | Reçoit les tickets, classifie, route |
| `agent-shipping.json` | Commandes non expédiées |
| `agent-delivery.json` | Produits non reçus |
| `agent-defect.json` | Produits défectueux |
| `agent-return.json` | Demandes de retour |
| `agent-cancellation.json` | Annulations après expédition |
| `human-validation.json` | File de validation humaine |
| `dashboard-stream.json` | Push events vers le dashboard |

## Variables d'environnement requises

Voir `.env.example` à la racine.
