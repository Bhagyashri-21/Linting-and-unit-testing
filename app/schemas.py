from pydantic import BaseModel, conint
from datetime import datetime
from typing import List, Optional


class TodoBase(BaseModel):
    task: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    assigned_by: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[conint(ge=0, le=3)] = None
    parent_id: Optional[int] = None


class TodoCreate(TodoBase):
    task: str
    assigned_by: str
    assigned_to: str
    group_id: Optional[int] = None


class groupsBase(BaseModel):
    name: str


class groupsCreate(groupsBase):
    pass


class groups(groupsBase):
    id: int
    todos: List[TodoBase] = []

    class Config:
        orm_mode = True


class Todo(TodoBase):
    id: int
    created_at: datetime
    group_id: Optional[int] = None
    subtasks: List["Todo"] = []

    class Config:
        orm_mode = True


class DeleteResponse(BaseModel):
    message: str
