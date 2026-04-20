# Project Brief — SAV Autonome Marketplace

## Problème

Les marchands sur marketplace passent jusqu'à 40% de leur temps support sur des cas SAV répétitifs et prévisibles (commande non expédiée, colis non reçu, produit défectueux, retour). Au pic (Black Friday, +130 commandes/sec sur les plateformes Mirakl), ce volume devient ingérable humainement.

## Solution

**Eugenia** — un système d'agents IA autonomes qui prend en charge le cycle de vie complet d'un ticket SAV : détection, analyse, décision, communication client, et résolution — sans intervention humaine pour les cas courants. Les cas critiques (remboursement, litige commercial) remontent à un humain avec un dossier complet pré-instruit.

## Périmètre UC1

| Catégorie SAV | Agent responsable | Autonomie |
|---|---|---|
| Commande non expédiée | `ShippingAgent` | Totale |
| Produit non reçu | `DeliveryAgent` | Totale |
| Produit défectueux | `DefectAgent` | Partielle (retour auto, remboursement → humain) |
| Annulation après expédition | `CancellationAgent` | Partielle |
| Demande de retour | `ReturnAgent` | Totale si dans les délais |

## Critères de succès (hackathon)

1. Démonstration end-to-end d'un ticket SAV traité autonomement en < 30 secondes
2. Dashboard marchand lisible par un non-développeur
3. Les agents expliquent leurs décisions à chaque étape
4. Un humain peut reprendre la main en 1 clic
5. Zéro remboursement déclenché sans validation humaine

## Non-périmètre

- Intégration réelle Mirakl API (mock uniquement)
- Multi-langue (FR uniquement pour le hackathon)
- Authentification multi-marchands
