from pathlib import Path
from tinydb import TinyDB, Query


class Config:

    def __init__(self):
        self.__config_path = Path(str(Path.home()) + '/.pmanager')
        self.__db_name = 'config'
        db_path = str(self.__config_path) + '/' + self.__db_name

        db_path = self.__db_name + '.json'

        self.__config_path.mkdir(parents=False, exist_ok=True)

        self.__db = TinyDB(db_path)
        self.__query = Query()

    def set_projects_path(self, value):
        self.__set_data('projects_path', value)

    def get_project_path(self):
        return self.__get_data('projects_path')

    def __get_data(self, key):
        return self.__db.search(self.__query.key == key)

    def __set_data(self, key, value):
        data = self.__db.search(self.__query.key == key)

        if data:
            self.__db.update({'value': value}, self.__query.key == key)
        else:
            self.__db.insert({'key': key, 'value': value})