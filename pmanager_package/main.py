import click
from pmanager_package.Models.Config import Config
from pmanager_package.Commands.Setup import Setup
from pmanager_package.Commands.Cli import Cli


config = Config()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(context):
    Cli.execute(context=context, config=config)


@cli.command()
def setup():
    Setup.execute(config)


if __name__ == '__main__':
    cli()
