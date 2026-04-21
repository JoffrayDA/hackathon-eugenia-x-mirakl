from __future__ import annotations
from datetime import datetime
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field
import uuid


def new_id() -> str:
    return str(uuid.uuid4())


# ── Core domain ──────────────────────────────────────────────────────────────

class ShippingInfo(BaseModel):
    carrier: str
    tracking_number: Optional[str] = None
    estimated_delivery: Optional[str] = None
    status: str  # "pending" | "shipped" | "delivered" | "lost"


class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    unit_price: float


class Order(BaseModel):
    id: str
    status: Literal["pending", "processing", "shipped", "delivered", "cancelled"]
    items: list[OrderItem]
    shipping: ShippingInfo
    merchant_id: str
    customer_id: str
    total_amount: float
    created_at: str
    sla_deadline: str


class Customer(BaseModel):
    id: str
    name: str
    email: str
    is_vip: bool = False
    order_count: int = 0


class MerchantPolicy(BaseModel):
    return_window_days: int = 30
    sla_shipping_hours: int = 48
    refund_threshold: float = 0.0  # 0 = tout passe par humain
    carriers: list[str] = []


class Merchant(BaseModel):
    id: str
    name: str
    policy: MerchantPolicy


# ── Agent events ──────────────────────────────────────────────────────────────

class AgentEvent(BaseModel):
    id: str = Field(default_factory=new_id)
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    ticket_id: str
    agent: str  # "orchestrator" | "shipping" | "delivery" | "defect" | "return" | "cancellation"
    action: str
    reasoning: str
    data: dict[str, Any] = {}
    requires_human: bool = False


# ── Human validation ──────────────────────────────────────────────────────────

class HumanValidation(BaseModel):
    id: str = Field(default_factory=new_id)
    ticket_id: str
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    status: Literal["pending", "approved", "rejected"] = "pending"
    amount: float
    reason: str
    agent_reasoning: str
    approved_amount: Optional[float] = None
    rejection_reason: Optional[str] = None
    resolved_at: Optional[str] = None


# ── Ticket ────────────────────────────────────────────────────────────────────

class Ticket(BaseModel):
    id: str = Field(default_factory=new_id)
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    customer: Customer
    order: Order
    type: Literal["unshipped", "not_received", "defective", "cancellation", "return", "unknown"] = "unknown"
    raw_message: str
    status: Literal["pending", "in_progress", "resolved", "escalated", "awaiting_human"] = "pending"
    confidence_score: int = 0
    agent_events: list[AgentEvent] = []
    resolution: Optional[str] = None
    human_validation_id: Optional[str] = None


# ── API schemas ───────────────────────────────────────────────────────────────

class IngestRequest(BaseModel):
    customer_message: str
    order_id: str


class IngestResponse(BaseModel):
    ticket_id: str
    status: str = "processing"


class ValidationApproveRequest(BaseModel):
    approved_amount: Optional[float] = None


class ValidationRejectRequest(BaseModel):
    reason: str


class OverrideRequest(BaseModel):
    action: Literal["pause", "take_over", "resume"]
    note: Optional[str] = None


class EmitEventRequest(BaseModel):
    event: AgentEvent
