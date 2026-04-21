import asyncio
from typing import AsyncGenerator
from models import AgentEvent
import json

# Global subscriber queues — one per connected SSE client
_subscribers: list[asyncio.Queue] = []

# In-memory state
tickets: dict = {}          # ticket_id → Ticket
validations: dict = {}      # validation_id → HumanValidation
paused_tickets: set = set() # ticket_ids paused by human override


async def subscribe() -> AsyncGenerator[str, None]:
    queue: asyncio.Queue = asyncio.Queue()
    _subscribers.append(queue)
    try:
        while True:
            event = await queue.get()
            yield event
    finally:
        _subscribers.remove(queue)


async def publish(event: AgentEvent) -> None:
    payload = f"data: {event.model_dump_json()}\n\n"
    for queue in _subscribers:
        await queue.put(payload)

    # Persist event on the ticket
    if event.ticket_id in tickets:
        tickets[event.ticket_id]["agent_events"].append(event.model_dump())
