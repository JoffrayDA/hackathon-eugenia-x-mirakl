# Hackathon Mirakl × Eugenia — UC1 : Agent Led Merchant SAV

Système d'agents IA autonomes pour gérer le SAV complet d'un marchand sur marketplace.
Les agents raisonnent, mémorisent chaque résolution, et deviennent plus performants à chaque ticket.

**Stack : n8n · Dust · OpenAI GPT-4o · Next.js**

---

## Structure du projet

```
├── agents/
│   ├── n8n/                 # Workflows n8n (exports JSON)
│   └── dust/                # Prompts agents + knowledge base
├── data/
│   ├── mock/                # Données simulées (commandes, clients, transporteurs)
│   └── scenarios/           # Scénarios de démo reproductibles
├── dashboard/               # Frontend marchand (Next.js)
├── backend/                 # API webhooks (FastAPI)
├── docs/                    # Documentation produit et technique
│   └── stories/             # Epics et stories de développement
└── deliverables/            # Livrables hackathon
```

---

## Qui fait quoi

| Dossier | Responsable suggéré |
|---|---|
| `agents/n8n/` | CAO — workflows automation |
| `agents/dust/` | CAIO — prompts et knowledge base |
| `data/` | CDO — données mock et scénarios |
| `dashboard/` | CPO — frontend et UX |
| `backend/` | CTO — API et webhooks |
| `docs/` | Tout le monde |

---

## Setup rapide

```bash
git clone https://github.com/[votre-repo]
cp .env.example .env
# Remplir les clés API dans .env
```

Voir le README de chaque dossier pour les instructions spécifiques.

---

## Règle absolue

> Aucun remboursement sans validation humaine explicite.

---

## Planning

| Jour | Objectif |
|---|---|
| Lun 20/04 | Golden Circle rendu 18h + Setup repo |
| Mar 21/04 | Agents n8n + Dust knowledge base |
| Mer 22/04 | Dashboard + Session biz Mirakl 14h |
| Jeu 23/04 | Polish + scénarios démo + documentation |
| Ven 24/04 | Rendu 8h + Pitch Mirakl 14h |
