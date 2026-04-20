# Epic 05 — Préparation Démo

**Priorité : CRITIQUE — Ne pas négliger (Jour 2 après-midi)**

---

## Story 5.1 — Scénarios démo scriptés
**Estimation : 45min**

Préparer 3 scénarios reproductibles dans `src/data/mock/scenarios.json` :

**Scénario A — "La démonstration parfaite" (golden path)**
- Ticket 1 : Commande non expédiée, SLA dépassé → agent résout seul en 15s
- Ticket 2 : Produit défectueux → agent propose remboursement → validation jury
- Ticket 3 : Demande de retour éligible → résolu en autonome

**Scénario B — "Sous pression" (volume)**
- 5 tickets arrivent en simultané → montrer que les agents parallélisent
- 3 résolus seuls, 2 en attente de validation

**Scénario C — "Reprise en main" (contrôle humain)**
- Ticket en cours → marchand override l'agent
- Marchand reprend la main, répond manuellement
- Montre que l'IA n'est pas une boîte noire

**Critère d'acceptance** : POST /demo/load-scenario/A|B|C → démo reproductible en 30s

---

## Story 5.2 — Polish UX démo
**Estimation : 1h**

Points critiques pour l'impression jury :
- [ ] Animations fluides sur les cards (60fps)
- [ ] Aucune erreur console visible
- [ ] Temps de réponse agents < 30s (ajouter des délais artificiels si trop rapide — le jury doit voir les agents "penser")
- [ ] Typographie propre, espacement cohérent
- [ ] Couleurs accessibles (pas de vert/rouge indistinguables)
- [ ] Mode sombre optionnel (si temps)
- [ ] Favicon + titre onglet "Eugenia — SAV Autonome"

---

## Story 5.3 — Script de pitch (non-tech)
**Estimation : 30min**

Document `docs/pitch.md` avec :
- Hook : "Aujourd'hui, un marchand passe X heures par semaine sur du SAV standard..."
- Demo flow : 3 minutes chrono
- Réponses aux questions difficiles :
  - "Que se passe-t-il si l'IA se trompe ?" → audit trail + override
  - "Et la RGPD ?" → données restent chez le marchand, pas de stockage externe
  - "Scalabilité ?" → architecture async, stateless agents
  - "Et Dust dans tout ça ?" → intégration optionnelle pour knowledge base marchand

---

## Ordre d'exécution recommandé

### Jour 1 — Matin (9h-12h)
1. Story 1.1 — Setup Backend
2. Story 1.2 — Données Mock
3. Story 1.3 — Setup Frontend
4. Story 1.4 — SSE

### Jour 1 — Après-midi (13h-18h)
5. Story 2.1 — Orchestrateur
6. Story 2.2 — ShippingAgent
7. Story 2.3 — DeliveryAgent
8. Story 3.1 — Endpoints Tickets
9. Story 3.2 — Endpoints Validations

### Jour 1 — Soir (18h-21h si courage)
10. Story 2.4 — DefectAgent
11. Story 2.5 — ReturnAgent
12. Story 2.6 — CancellationAgent

### Jour 2 — Matin (9h-12h)
13. Story 4.1 — Layout
14. Story 4.2 — Flux Live ← priorité absolue UX
15. Story 4.4 — Validations Humaines ← priorité absolue métier

### Jour 2 — Après-midi (13h-16h)
16. Story 4.3 — File SAV
17. Story 4.5 — Détail Ticket
18. Story 5.1 — Scénarios démo
19. Story 5.2 — Polish

### Jour 2 — Buffer (16h-18h)
20. Story 3.3 — Override
21. Story 4.6 — Stats
22. Story 5.3 — Pitch script
23. Tests end-to-end des 3 scénarios
