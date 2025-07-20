from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from .service import list_todos, create_todo

app = Flask(__name__)

# Setup DB
engine = create_engine('sqlite:///todos.db')
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

@app.route('/todos', methods=['GET'])
def get_todos():
    session = SessionLocal()
    todos = list_todos(session)
    return jsonify([{"id": t.id, "title": t.title, "desc": t.description} for t in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    session = SessionLocal()
    try:
        todo = create_todo(session, data['title'], data.get('description', ''))
        return jsonify({"id": todo.id, "title": todo.title}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
