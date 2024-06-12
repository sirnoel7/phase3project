import click
import datetime
from cli import add_category, add_task, view_tasks, mark_task_complete, delete_task

@click.group()
def app():
    pass

@app.command()
def addtask():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    category_name = input("Enter category name: ")
    
    add_category(category_name)
    
    # this converts the due_date string to datetime.date object
    due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
    
    add_task(title, description, due_date, category_name)

@app.command()
def viewtasks():
    view_tasks()

@app.command()
def complete():
    view_tasks()
    task_id = int(input("Enter task ID to mark as complete: "))
    mark_task_complete(task_id)

@app.command()
def deletetask():
    view_tasks()
    task_id = int(input("Enter task ID to delete: "))
    delete_task(task_id)

if __name__ == '__main__':
    click.echo("Welcome to the To-Do List Application!")
    while True:
        click.echo("What would you like to do?")
        click.echo("1. Add a task")
        click.echo("2. View tasks")
        click.echo("3. Mark a task as complete")
        click.echo("4. Delete a task")
        click.echo("5. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addtask()
        elif choice == "2":
            viewtasks()
        elif choice == "3":
            complete()
        elif choice == "4":
            deletetask()
        elif choice == "5":
            break
        else:
            click.echo("Invalid choice. Please enter a valid option.")
