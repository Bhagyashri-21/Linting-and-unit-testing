from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()


@router.post("/create/groups/", response_model=schemas.groups)
def create_group(
        group: schemas.groupsCreate,
        db: Session = Depends(database.get_db)):
    try:
        return crud.create_todo_group(db, group)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error creating group: {e}")


@router.get("/list/groups/")
def list_groups(
        db: Session = Depends(database.get_db)):
    try:
        return crud.get_todo_groups(db)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error fetching groups: {e}")


@router.get("/get/groups/{group_id}", response_model=schemas.groups)
def get_group(group_id: int, db: Session = Depends(database.get_db)):
    group = crud.get_todo_group_by_id(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.post("/create/todos/", response_model=schemas.Todo)
def create_task(
        todo: schemas.TodoCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_todo(db, todo)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error creating todo: {e}")


@router.get("/get/grouped/todos", response_model=list[schemas.groups])
def get_grouped_todos(db: Session = Depends(database.get_db)):
    try:
        return crud.get_todo_groups(db)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error fetching grouped todos: {e}")


@router.put("/update/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(
        todo_id: int,
        todo: schemas.TodoBase,
        db: Session = Depends(database.get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.delete("/delete/todos/{todo_id}",
               response_model=schemas.DeleteResponse)
def delete_task(todo_id: int, db: Session = Depends(database.get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}


@router.delete("/delete/groups/{group_id}",
               response_model=schemas.DeleteResponse)
def delete_group(group_id: int, db: Session = Depends(database.get_db)):
    db_group = crud.delete_todo_group(db, group_id)
    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group deleted successfully"}


@router.get("/list/todos/", response_model=list[schemas.Todo])
def list_all_tasks(db: Session = Depends(database.get_db)):
    try:
        return crud.get_all_todos(db)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error fetching todos: {e}"
        )
