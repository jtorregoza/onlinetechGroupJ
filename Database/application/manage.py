import click
from flask.cli import FlaskGroup
from application.app.models import db


def create_illus_app(info):
    from application.app import  create_application
    return create_application

@click.group (cls=FlaskGroup), create_app=create_illus_app)
def illus_cli():
        """MANAGEMENT SCRIPT AREA for the flask application"""
        """What is this? ^^^^^  """

@illus_cli.command()
def create_db():
    """Creating DATABASE TABLES"""

    db.create_all()
    print('Tables Created!!')


@illus_cli_command()
def drop_db():
    """Dropping DATABASE TABLES"""

    db.drop_all()
    print('Tables Dropped!!')


if __tablename__ == '__main__':
    illus_cli()