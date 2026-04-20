# Epic 02 — Agents IA

**Priorité : CRITIQUE — Cœur du produit (Jour 1 après-midi)**

---

## Story 2.1 — Orchestrateur Agent
**Estimation : 1h**

Agent GPT-4o avec function calling qui :
1. Reçoit un ticket brut (message client + données commande)
2. Classifie le type SAV avec score de confiance
3. Route vers l'agent spécialisé approprié
4. Émet un `AgentEvent` "classified" visible en dashboard

Tools disponibles :
- `get_order_details(order_id)` → Order
- `get_customer_history(customer_id)` → Customer + historique
- `emit_event(event)` → push SSE
- `escalate_to_human(reason, confidence)` → si < 70%

Prompt système : voir `docs/architecture.md#orchestrateur`

**Critère d'acceptance** : POST /tickets/ingest avec message "mon colis n'est pas arrivé" → event SSE reçu avec type classifié correctement

---

## Story 2.2 — ShippingAgent (Commande non expédiée)
**Estimation : 45min**

Agent spécialisé qui :
1. Récupère le statut de commande et la date SLA
2. Si dans les délais : envoie message client rassurant avec ETA
3. Si SLA dépassé : relance transporteur + message client + notifie marchand
4. Émet events à chaque étape

Tools :
- `check_order_shipping_status(order_id)`
- `get_merchant_sla(merchant_id)`
- `send_customer_email(customer_id, message)`
- `request_carrier_followup(tracking_number)` → mock
- `emit_event(event)`

**Critère d'acceptance** : Ticket "ma commande n'a pas été expédiée" sur une commande en retard → 3+ events SSE, email client généré, marchand notifié

---

## Story 2.3 — DeliveryAgent (Produit non reçu)
**Estimation : 45min**

Agent spécialisé qui :
1. Vérifie statut transporteur (mock)
2. Si en transit : informe client + ETA
3. Si livré selon transporteur : demande vérification client, propose recours
4. Si perdu (> délai max) : ouvre déclaration + propose renvoi OU remboursement → validation humaine

Tools :
- `check_carrier_status(tracking_number)` → mock
- `open_loss_declaration(order_id)` → mock
- `propose_reshipment(order_id)`
- `request_refund_validation(order_id, amount, reason)` → → HumanValidationQueue
- `emit_event(event)`

**Critère d'acceptance** : Ticket sur commande "perdue" → validation humaine créée avec contexte complet

---

## Story 2.4 — DefectAgent (Produit défectueux)
**Estimation : 1h**

Agent spécialisé qui :
1. Analyse la description du problème (et photo si fournie)
2. Vérifie éligibilité retour (politique marchand)
3. Propose : retour + renvoi (autonome) OU retour + remboursement (→ humain)
4. Si retour : génère bon de retour mock

Tools :
- `analyze_defect_description(description, photo_url?)` → LLM analysis
- `check_return_eligibility(order_id, merchant_id)`
- `generate_return_label(order_id)` → mock PDF
- `request_refund_validation(order_id, amount, reason)`
- `emit_event(event)`

**Critère d'acceptance** : Ticket "produit cassé" sur commande récente → bon de retour généré + validation remboursement créée

---

## Story 2.5 — ReturnAgent (Demande de retour)
**Estimation : 45min**

Agent spécialisé qui :
1. Vérifie que la commande est dans le délai de retour
2. Si éligible : génère bon de retour + instruit remboursement → validation humaine
3. Si inéligible : répond client avec explication + proposition commerciale (avoir)

Tools :
- `check_return_window(order_id, merchant_id)`
- `generate_return_label(order_id)`
- `request_refund_validation(order_id, amount, reason)`
- `offer_store_credit(customer_id, amount)` → autonome
- `emit_event(event)`

**Critère d'acceptance** : Ticket retour éligible → bon de retour généré + validation humaine en attente. Ticket hors délai → message refus avec offre avoir.

---

## Story 2.6 — CancellationAgent (Annulation après expédition)
**Estimation : 45min**

Agent spécialisé qui :
1. Vérifie si le colis est encore interceptable (non livré)
2. Si interceptable : contacte transporteur pour retour expéditeur
3. Si livré : lance procédure de retour automatique
4. Remboursement → toujours validation humaine

Tools :
- `check_carrier_status(tracking_number)`
- `request_carrier_intercept(tracking_number)` → mock
- `initiate_return_process(order_id)`
- `request_refund_validation(order_id, amount, reason)`
- `emit_event(event)`

**Critère d'acceptance** : Annulation sur colis en transit → demande interception + validation remboursement créée
