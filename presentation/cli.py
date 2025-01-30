# presentation/cli.py
import click
from entities.services import todo_service
from infrastructure.repository import FileRepository

# File location for the repository
FILE_PATH = "database/tasks.txt"

@click.group()
def cli():
    """The main command group for the To-Do app."""
    pass

@cli.command()
@click.argument("task")
def add(task):
    """Add a new task to the list."""
    try:
        repository = FileRepository(FILE_PATH)
        service = todo_service(repository)
        service.add_task(task)
        click.echo(f"Task added: {task}")
    except Exception as e:
        click.echo(f"Error adding task: {e}")

@cli.command()
def list():
    """List all tasks."""
    try:
        repository = FileRepository(FILE_PATH)
        service = todo_service(repository)
        tasks = service.show_list()
        if tasks:
            click.echo("Your tasks:")
            for i, task in enumerate(tasks):
                click.echo(f"{i}. {task}")
        else:
            click.echo("No tasks found.")
    except Exception as e:
        click.echo(f"Error retrieving tasks: {e}")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Delete a task by its index."""
    try:
        repository = FileRepository(FILE_PATH)
        service = todo_service(repository)
        service.delete_task(index)
        click.echo(f"Task {index} deleted.")
    except IndexError:
        click.echo(f"Error: Task index {index} is out of range.")
    except Exception as e:
        click.echo(f"Error deleting task: {e}")
