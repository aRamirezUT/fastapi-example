# Create model
from datetime import datetime
from pydantic import BaseModel
from sqlmodel import SQLModel
from backend.models.campaigns import Campaign

class CampaignCreate(SQLModel):
    name: str
    due_date: datetime | None = None

class CampaignSingleResponse(BaseModel):
    campaigns: Campaign