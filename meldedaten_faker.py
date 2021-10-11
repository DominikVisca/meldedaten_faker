import click
from app import application

@click.group()
def cli():
    pass

@cli.command()
def generate():
    """Generates fake census data"""
    application.generate()