import click
from pathlib import Path
from pmanager_package import log


class Setup:

    @staticmethod
    def execute(config):
        config.set_projects_path(
            click.prompt(
                "Please provide your projects location",
                default=str(Path.home()) + '/Projects'
            )
        )