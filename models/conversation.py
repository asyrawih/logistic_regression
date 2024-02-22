from dataclasses import dataclass


@dataclass
class Messages:
    sender: str
    timestamp: str
    message: str


@dataclass
class Converstion:
    customer_id: int
    conversation_id: str
    messages: list[Messages]
    withdrawal_limit_increase_requested: bool


@dataclass
class Conversations:
    conversations: list[Converstion]
