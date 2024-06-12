import click
import datetime
from cli import add_category, add_task, view_tasks, mark_task_complete, delete_task

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def addcategory(name):
    add_category(name)

@cli.command()
@click.argument('title')
@click.argument('description')
@click.argument('due_date')
@click.argument('category_id', type=int)
def addtask(title, description, due_date, category_id):
    due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
    add_task(title, description, due_date, category_id)

@cli.command()
def viewtasks():
    view_tasks()

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    mark_task_complete(task_id)

@cli.command()
@click.argument('task_id', type=int)
def deletetask(task_id):
    delete_task(task_id)

if __name__ == '__main__':
    cli()
