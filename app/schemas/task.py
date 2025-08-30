from typing import Optional
from pydantic import BaseModel ,Field
from datetime import datetime, time, date


class createTeam(BaseModel):
    date : date
    entity_name: str
    task_type: str
    time: time
    contact_person: str
    note: str
    status: str = Field(default="Close") 


class deleteteam(BaseModel):
    id :str