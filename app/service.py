from .repository import get_all_todos, add_todo

def list_todos(session):
    return get_all_todos(session)

def create_todo(session, title, description):
    if not title:
        raise ValueError("Title is required")
    return add_todo(session, title, description)
