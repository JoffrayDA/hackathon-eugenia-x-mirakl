# EUGENIA — Decision Log

**Session :** Roundtable Party Mode (Mary, John, Winston, Sally)
**Date :** 21 avril 2026
**Présentation jury :** Vendredi 25 avril 2026

---

## VALIDÉ — On ne revient pas dessus

| # | Décision |
|---|----------|
| V-01 | **RB-01 est une règle dure et le différenciateur clé du pitch** — aucun remboursement sans validation humaine, jamais contournable |
| V-02 | L'audit trail (traçabilité de chaque décision agent en français clair) est un différenciateur réel, pas un nice-to-have |
| V-03 | Les données mockées sont un choix délibéré de prototypage — à positionner comme tel dans le pitch, pas comme une limitation |
| V-04 | La métrique d'impact merchant quantifiée est une priorité du pitch — le chiffre doit être défini avant vendredi |
| V-05 | Les 5 agents sont justifiés par le besoin utilisateur, pas par l'élégance architecturale |
| V-06 | Architecture validée : FastAPI + GPT-4o + Next.js 14 + SSE + snapshot JSON pour la persistance d'état |

---

## DÉCIDÉ — Ce qu'on fait et comment

| # | Décision | Deadline |
|---|----------|----------|
| D-01 | Interface contracts entre agents à définir avant tout code (input/output par agent, protocole de routage orchestrateur) | Mardi soir |
| D-02 | Dashboard design : métriques émotionnelles, clair, non écrasant — north star : Karim voit en 10 secondes ce qui brûle | Mercredi |
| D-03 | La ValidationCard est l'élément UI central pour RB-01 — c'est l'écran à perfectionner en priorité | Mercredi |
| D-04 | Scénarios GPT-4o pré-cachés pour limiter la latence en démo | Mercredi |
| D-05 | Scope chirurgical : zéro feature creep sans accord collectif — toute nouvelle feature peut être vetée | Continu |

---

## PERSONA PRINCIPALE — North Star

> **Karim, 34 ans, responsable SAV chez un marchand mid-size sur Mirakl, qui gère 80 tickets/jour seul, et qui a besoin de savoir en 10 secondes ce qui brûle et ce qui attend sa signature.**

Toute décision UX se filtre par : *est-ce que ça aide Karim à décider plus vite, ou est-ce que ça l'encombre ?*

---

## QUESTIONS OUVERTES

| # | Question | Responsable | Deadline |
|---|----------|-------------|----------|
| Q-01 | Quel est le chiffre d'impact merchant ? (benchmark Mirakl / Gorgias / Zendesk) | John + Mary | Mardi |
| Q-02 | Comment présenter l'orchestrateur au jury sans tomber dans la complexité technique ? | John | Jeudi |
| Q-03 | Quel est le hero scenario de démo (RB-01 + validation humaine en live de bout en bout) ? | Toute l'équipe | Mercredi |

---

## NEXT ACTIONS

```
MARDI
  → Winston : rédiger les interface contracts (input/output par agent)
  → John + Mary : trouver le benchmark chiffré pour la métrique merchant

MERCREDI
  → Sally : maquettes dashboard + ValidationCard
  → Winston : liste des scénarios pré-cachés GPT-4o
  → Équipe : aligner sur le hero scenario de démo

JEUDI
  → Feature freeze
  → Répétition pitch complète (timing, narration, démo live)

VENDREDI
  → Jury
```

---

## RÈGLE D'OR

> Scope chirurgical jusqu'au jury. Si quelqu'un propose une nouvelle feature, la question est : *est-ce que ça aide Karim à décider en 10 secondes ?* Si la réponse n'est pas oui immédiatement — ça sort.
