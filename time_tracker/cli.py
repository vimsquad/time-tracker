import click
from .main import TimeTracker


@click.command()
@click.version_option(package_name="time-tracker")
def cli():
    """Time Tracker Program"""
    t = TimeTracker()
    print("click interface")


if __name__ == "__main__":
    cli()
