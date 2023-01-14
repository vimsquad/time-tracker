import click


@click.command()
@click.version_option(package_name="time-tracker")
def cli():
    """Simple program that greets NAME for a total of COUNT times."""
    print("click interface")


if __name__ == "__main__":
    cli()
