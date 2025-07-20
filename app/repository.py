from sqlalchemy.orm import Session
from .models import Todo

def get_all_todos(session: Session):
    return session.query(Todo).all()

def add_todo(session: Session, title: str, description: str):
    todo = Todo(title=title, description=description)
    session.add(todo)
    session.commit()
    return todo
