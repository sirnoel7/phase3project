import datetime
from sqlalchemy.orm import sessionmaker
from models import init_db, Task, Category

engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()

def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' added.")

def add_task(title, description, due_date, category_id):
    task = Task(title=title, description=description, due_date=due_date, category_id=category_id)
    session.add(task)
    session.commit()
    print(f"Task '{title}' added.")

def view_tasks():
    tasks = session.query(Task).all()
    task_list = [(task.id, task.title, task.description, task.due_date, task.status) for task in tasks]
    for task in task_list:
        print(f"{task[0]}. {task[1]} - {task[2]} - Due: {task[3]} - Status: {'Completed' if task[4] else 'Pending'}")

def mark_task_complete(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    task.status = True
    session.commit()
    print(f"Task '{task.title}' marked as complete.")

def delete_task(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    session.delete(task)
    session.commit()
    print(f"Task '{task.title}' deleted.")
