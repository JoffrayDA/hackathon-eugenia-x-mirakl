# Dust Agents

## Structure

### `prompts/`
Prompts systèmes de chaque agent Dust. À copier-coller dans la configuration Dust.

| Fichier | Agent Dust |
|---|---|
| `orchestrator.md` | Agent Orchestrateur |
| `shipping.md` | Agent Expédition |
| `delivery.md` | Agent Livraison |
| `defect.md` | Agent Défauts |
| `return.md` | Agent Retours |
| `cancellation.md` | Agent Annulations |

### `knowledge-base/`
Données initiales à importer dans la knowledge base Dust.

| Fichier | Contenu |
|---|---|
| `merchant-policies.md` | Politiques SAV marchand (SLA, retours, remboursements) |
| `carrier-procedures.md` | Procédures transporteurs (GLS, Colissimo, DHL) |
| `resolved-cases.json` | Cas résolus initiaux pour amorcer l'apprentissage |

## Setup Dust

1. Créer un workspace Dust avec le compte hackathon.eugenia@gmail.com
2. Créer une knowledge base "SAV Memory"
3. Importer les fichiers du dossier `knowledge-base/`
4. Créer les agents avec les prompts du dossier `prompts/`
5. Copier les IDs dans `.env`
