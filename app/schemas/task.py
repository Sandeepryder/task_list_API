from typing import Optional
from pydantic import BaseModel ,Field
from datetime import datetime, time, date


class createTeam(BaseModel):
    date : str
    entity_name: str
    task_type: str
    time: str
    contact_person: str
    note: str
    status: str


class deleteteam(BaseModel):
    id :str


class StatusUpdate(BaseModel):
    id: str
    status: str


class TeamEdit(BaseModel):
    id: str
    date: str
    entity_name: str
    task_type: str
    time: str
    contact_person: str
    note: str
    status: str