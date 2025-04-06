from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
from . import models, schemas


def create_todo_group(db: Session, group: schemas.groupsCreate):
    """ Create a Todo Group"""
    db_group = models.GroupDB(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def create_todo(db: Session, todo: schemas.TodoCreate):
    """Create a Todo"""
    db_todo = models.TodoItemDB(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todo_groups(db: Session):
    """Retrieve all Todo Groups"""
    return db.query(
        models.GroupDB).options(
            joinedload(models.GroupDB.todos)).order_by(
                desc(models.GroupDB.id)).all()


def get_todo_group_by_id(db: Session, group_id: int):
    """Retrieve a specific Todo Group by ID"""
    return db.query(
        models.GroupDB).filter(models.GroupDB.id == group_id).first()


def get_todo_by_id(db: Session, todo_id: int):
    """Retrieve a specific Todo by ID"""
    return db.query(
        models.TodoItemDB).filter(models.TodoItemDB.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoBase):
    """Update a Todo"""
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        for key, value in todo_update.dict(exclude_unset=True).items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    """Delete a Todo"""
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return db_todo
    return None


def delete_todo_group(db: Session, group_id: int):
    group = db.query(
        models.GroupDB).filter(models.GroupDB.id == group_id).first()
    if group:
        db.delete(group)
        db.commit()
        return group
    return None


def get_all_todos(db: Session):
    return db.query(models.TodoItemDB).all()
