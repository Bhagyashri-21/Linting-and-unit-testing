from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class GroupDB(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    todos = relationship("TodoItemDB",
                         back_populates="group",
                         cascade="all, delete-orphan")


class TodoItemDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    assigned_by = Column(String)
    assigned_to = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True)
    priority = Column(Integer, nullable=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=True)
    group = relationship("GroupDB", back_populates="todos")
    parent_id = Column(Integer, ForeignKey("todos.id"),
                       nullable=True)  # Parent id == task id
    parent = relationship("TodoItemDB", remote_side=[id],
                          backref="subtasks")  #
