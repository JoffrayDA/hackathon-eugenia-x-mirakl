from fastapi import APIRouter, HTTPException, BackgroundTasks
from data.loader import get_scenarios, get_orders, get_customers
from models import Ticket, Customer, Order
from services import event_bus

router = APIRouter(prefix="/demo")


@router.get("/scenarios")
async def list_scenarios():
    scenarios = get_scenarios()
    return [{"id": k, "name": v["name"], "description": v["description"]} for k, v in scenarios.items()]


@router.post("/load-scenario/{scenario_id}")
async def load_scenario(scenario_id: str, background_tasks: BackgroundTasks):
    scenarios = get_scenarios()
    if scenario_id not in scenarios:
        raise HTTPException(status_code=404, detail=f"Scenario '{scenario_id}' not found. Available: {list(scenarios.keys())}")

    scenario = scenarios[scenario_id]
    orders = get_orders()
    customers = get_customers()
    created_tickets = []

    for ticket_def in scenario["tickets"]:
        order_id = ticket_def["order_id"]
        order_data = orders.get(order_id)
        if not order_data:
            continue
        customer_data = customers.get(order_data["customer_id"])
        if not customer_data:
            continue

        ticket = Ticket(
            customer=Customer(**customer_data),
            order=Order(**order_data),
            raw_message=ticket_def["message"],
            type=ticket_def.get("type", "unknown"),
        )
        event_bus.tickets[ticket.id] = ticket.model_dump()
        created_tickets.append(ticket.id)

    return {"ok": True, "scenario": scenario_id, "tickets_created": created_tickets}


@router.post("/reset")
async def reset_demo():
    event_bus.tickets.clear()
    event_bus.validations.clear()
    event_bus.paused_tickets.clear()
    return {"ok": True, "message": "Demo state reset"}
