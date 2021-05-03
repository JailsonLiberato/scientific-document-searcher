from jproperties import Properties


class PropertyUtils:

    CONST_DATA_PROPERTY: int = 0

    def __init__(self, filename='configurations.properties'):
        self.__configs = Properties()
        self.__filename = filename
        self.__load_file()

    def __load_file(self):
        with open(self.__filename, 'rb') as config_file:
            self.__configs.load(config_file)

    def get_property(self, prop: str) -> str:
        return self.__configs.get(prop)[self.CONST_DATA_PROPERTY]
