import click
from pmanager_package.Models.Config import Config
from pmanager_package.Commands.Cli import Cli
from pmanager_package.Commands.Setup import Setup


config = Config()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(context):
    Cli.execute(context=context, config=config)


@cli.command()
@click.option('-p', '--projects-path', help="Path to Projects folder.")
@click.option('-d', '--docker-path', help="Path to docker proxy folder.")
@click.option('-r', '--docker-repository', help="A repository to use to instantiate the proxy. Leave empty to use default.")
def setup(projects_path, docker_path, docker_repository):
    Setup.execute(config, {
        'projects_path': projects_path,
        'docker_proxy_path': docker_path,
        'docker_proxy_repository': docker_repository
    })


if __name__ == '__main__':
    cli()
