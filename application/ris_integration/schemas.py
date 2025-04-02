from pydantic import BaseModel
from typing import Optional


class RisRequest(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    campaign_id: Optional[str] = None
    url: Optional[str] = None
