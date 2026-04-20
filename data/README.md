# Data Mock

## `mock/`
Données statiques simulant l'environnement Mirakl Connect.

| Fichier | Description |
|---|---|
| `orders.json` | 20 commandes (tous statuts couverts) |
| `customers.json` | 10 clients (dont 2 VIP) |
| `merchant.json` | 1 marchand avec politiques SAV complètes |
| `carriers.json` | Réponses simulées GLS / Colissimo / DHL |

## `scenarios/`
Scénarios de démo reproductibles.

| Fichier | Description |
|---|---|
| `scenario-A.json` | Golden path — 3 tickets résolus en autonomie |
| `scenario-B.json` | Volume — 5 tickets simultanés |
| `scenario-C.json` | Reprise en main — override humain en live |
