import click
from pathlib import Path
from pmanager_package import log
from pmanager_package.Models.Config import Config
from git import Repo


class Setup:

    def __init__(self, config: Config, data: dict):
        self.__config = config
        self.__data = data
        self.__defaults = {
            'projects_path': {
                'prompt': 'Path to Projects folder',
                'default': str(Path.home()) + '/Projects'
            },
            'docker_proxy_path': {
                'prompt': 'Path to docker proxy folder.',
                'default': str(Path.home()) + '/Projects/docker'
            }
        }

    def run(self):
        for key, value in self.__data.items():
            value = self.__check_value(key, value)
            self.__set_data(key, value)

        self.__clone_docker()

    def __check_value(self, key: str, value):
        if key == 'docker_proxy_repository' and value is None:
            return self.__ask_for_docker()

        if value:
            return value

        value = self.__config.get_data(key)

        if not value:
            value = self.__defaults[key]['default']

        value = click.prompt(self.__defaults[key]['prompt'], value)

        return value

    def __ask_for_docker(self):
        if click.confirm("Do you have a docker proxy repository to clone?"):
            return click.prompt("The url for your docker repository [i.e. git@github.com:commax89/pmanager.git]")
        else:
            return "git@github.com:commax89/pmanager.git"

    def __clone_docker(self):
        if Path(self.__config.get_data('docker_proxy_path')).exists():
            return

        log.info("Cloning repo.")
        Repo.clone_from(
            self.__config.get_data('docker_proxy_repository'),
            self.__config.get_data('docker_proxy_path')
        )
        log.info("Finished cloning repo.")

    def __set_data(self, key, value):
        self.__config.set_data(key, value)

    @staticmethod
    def execute(config: Config, data: dict):
        setup = Setup(config, data)
        setup.run()