# PRD — Eugenia : SAV Autonome Marketplace

## Vision Produit

> "Un marchand ne devrait jamais avoir à lire un ticket SAV standard. Les agents s'en occupent, lui montrent ce qu'ils font, et ne lui demandent que ce que seul un humain peut décider."

## Personas

### 1. Le Marchand (utilisateur principal)
- PME ou ETI vendant sur marketplace (Fnac, Galeries Lafayette, etc.)
- Pas développeur, gère son SAV depuis un dashboard web
- Veut : gain de temps, zéro erreur sur les remboursements, visibilité sur ce que font les agents

### 2. L'Agent Support Humain (escalade)
- Reçoit uniquement les cas critiques pré-instruits
- Valide ou rejette une décision d'agent en 1 clic avec contexte complet

---

## Fonctionnalités

### F1 — Intake et Triage automatique
- Les tickets entrants (email simulé / form) sont classifiés automatiquement par type SAV
- Score de confiance affiché sur le dashboard
- Durée cible : < 3 secondes par ticket

### F2 — Agents de résolution spécialisés
Chaque agent a accès à : historique commande, politique marchand, historique client, transporteur mock.

**F2.1 ShippingAgent** — Commande non expédiée
- Vérifie délai de traitement vs SLA marchand
- Si dépassé : envoie relance transporteur (mock) + notifie client
- Si délai OK : informe client avec ETA mis à jour

**F2.2 DeliveryAgent** — Produit non reçu
- Vérifie statut transporteur (mock)
- Si perdu : ouvre déclaration de perte + propose renvoi ou remboursement
- Si en transit : rassure client avec suivi actualisé

**F2.3 DefectAgent** — Produit défectueux
- Analyse description + photo (si fournie)
- Propose : retour + renvoi, ou retour + remboursement (→ validation humaine)
- Génère étiquette retour (mock)

**F2.4 CancellationAgent** — Annulation après expédition
- Si colis non livré : contacte transporteur pour interception (mock)
- Si livré : lance procédure de retour automatique
- Remboursement → toujours validation humaine

**F2.5 ReturnAgent** — Demande de retour
- Vérifie éligibilité (délai, état produit selon politique marchand)
- Si éligible : génère bon de retour + instruite remboursement → validation humaine
- Si inéligible : répond client avec explication + proposition commerciale

### F3 — Communication client automatique
- Chaque action agent génère un message client en langage naturel
- Ton adapté (professionnel, empathique pour les défauts)
- Le marchand voit le message avant envoi (mode preview)

### F4 — Dashboard Marchand
- **Vue Flux Live** : timeline des actions agents en temps réel (type "chat entre agents")
- **Vue File d'attente** : tous les tickets avec statut (En cours / Résolu / Escaladé)
- **Vue Validation humaine** : cas en attente avec contexte complet + bouton Approuver/Rejeter
- **Vue Ticket détail** : audit trail complet de toutes les décisions agents + justifications

### F5 — Escalade et Human-in-the-Loop
- Tout remboursement → card de validation avec : montant, raison, historique client, recommandation agent
- Timeout de 4h → reminder automatique
- Le marchand peut override n'importe quel agent à n'importe quelle étape

---

## Règles Métier Critiques

| Règle | Description |
|---|---|
| RB-01 | Aucun remboursement sans validation humaine explicite |
| RB-02 | Un agent ne peut pas modifier une commande déjà escaladée |
| RB-03 | Délai max de résolution autonome : 48h (sinon escalade automatique) |
| RB-04 | Score confiance < 70% → escalade automatique |
| RB-05 | Client VIP (> 5 commandes) → toujours notifier le marchand même si résolu |

---

## Métriques de succès (démo)

- Taux de résolution autonome : cible > 80% des tickets mock
- Temps moyen de traitement agent : < 30s par ticket
- Aucun faux positif sur les remboursements (RB-01)
