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

    def get_data(self, key):
        doc = self.__db.get(self.__query.key == key)

        if not doc:
            return None

        return doc['value']

    def set_data(self, key, value):
        self.__db.upsert({'key': key, 'value': value}, self.__query.key == key)