from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Session(BaseModel):
    pass


@dataclass
class IncreseWithdrawLimit(BaseModel):
    pass
