import click
from app import application

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def generate(path):
    """Generates fake census data"""
    application.generate(path)