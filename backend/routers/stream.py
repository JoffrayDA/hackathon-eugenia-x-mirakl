from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from services import event_bus

router = APIRouter()


@router.get("/stream")
async def stream():
    return StreamingResponse(
        event_bus.subscribe(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@router.post("/events/emit")
async def emit_event(body: dict):
    from models import AgentEvent
    event = AgentEvent(**body["event"])
    await event_bus.publish(event)
    return {"ok": True}
