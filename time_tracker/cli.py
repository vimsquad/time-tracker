import click
from .main import TimeTracker


@click.group()
@click.version_option(package_name="time-tracker")
def cli():
    """Time Tracker Program"""


@cli.command()
@click.option("description", "-d", help="Description of Event")
@click.option("category", "-c", help="Category of Entry")
@click.option("status", "-s", help="Status of Entry")
def add_entry(description, category, status):
    """Adds Time entry"""
    time_tracker = TimeTracker(data_store_type="json")
    time_tracker.add_entry(description=description, category=category, status=status)


if __name__ == "__main__":
    cli()
