import click
from pmanager_package import utils
from tinydb import TinyDB, Query
from pathlib import Path

@click.group(invoke_without_command=True)
@click.pass_context
def cli(context):
    is_setup = context.invoked_subcommand and context.invoked_subcommand == 'setup'

    if is_setup:
        return

    db = TinyDB('db.json')
    config = Query()

    project_path = db.search(config.path == 'project/path')
    if not project_path:
        context.fail("There is no setup yet. Please run 'pmanager_package setup'")


@cli.command()
def setup():
    db = TinyDB('db.json')

    projects_path = str(Path.home()) + '/Projects'

    projects_path = click.prompt("Please provide your projects location", default=projects_path)

    utils.info("Your projects path is: " + projects_path)

    db.insert({'path': 'project/path', 'value': projects_path})