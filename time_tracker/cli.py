import click


@click.command()
@click.version_option(package_name="time-tracker")
def cli():
    """Time Tracker Program"""
    print("click interface")


if __name__ == "__main__":
    cli()
