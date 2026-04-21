from fastapi import APIRouter, HTTPException
from models import HumanValidation, ValidationApproveRequest, ValidationRejectRequest, AgentEvent
from services import event_bus
from datetime import datetime

router = APIRouter(prefix="/validations")


@router.get("")
async def list_validations(status: str = "pending"):
    return [v for v in event_bus.validations.values() if v["status"] == status]


@router.get("/{validation_id}")
async def get_validation(validation_id: str):
    if validation_id not in event_bus.validations:
        raise HTTPException(status_code=404, detail="Validation not found")
    return event_bus.validations[validation_id]


@router.post("/{validation_id}/approve")
async def approve_validation(validation_id: str, body: ValidationApproveRequest):
    if validation_id not in event_bus.validations:
        raise HTTPException(status_code=404, detail="Validation not found")

    v = event_bus.validations[validation_id]
    v["status"] = "approved"
    v["approved_amount"] = body.approved_amount or v["amount"]
    v["resolved_at"] = datetime.utcnow().isoformat()

    ticket_id = v["ticket_id"]
    if ticket_id in event_bus.tickets:
        event_bus.tickets[ticket_id]["status"] = "resolved"

    event = AgentEvent(
        ticket_id=ticket_id,
        agent="human",
        action="human_approved",
        reasoning=f"Remboursement de {v['approved_amount']}€ approuvé par le marchand.",
        data={"approved_amount": v["approved_amount"]},
        requires_human=False,
    )
    await event_bus.publish(event)
    return {"ok": True, "approved_amount": v["approved_amount"]}


@router.post("/{validation_id}/reject")
async def reject_validation(validation_id: str, body: ValidationRejectRequest):
    if validation_id not in event_bus.validations:
        raise HTTPException(status_code=404, detail="Validation not found")

    v = event_bus.validations[validation_id]
    v["status"] = "rejected"
    v["rejection_reason"] = body.reason
    v["resolved_at"] = datetime.utcnow().isoformat()

    ticket_id = v["ticket_id"]
    if ticket_id in event_bus.tickets:
        event_bus.tickets[ticket_id]["status"] = "resolved"

    event = AgentEvent(
        ticket_id=ticket_id,
        agent="human",
        action="human_rejected",
        reasoning=f"Remboursement refusé par le marchand. Raison : {body.reason}",
        data={"reason": body.reason},
        requires_human=False,
    )
    await event_bus.publish(event)
    return {"ok": True}
