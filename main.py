from utils.property_utils import PropertyUtils


class Main:

    def __init__(self):
        self.__property_util = PropertyUtils()
        self.__core_key = self.__property_util.get_property('core_key')
        print(self.__core_key)

    def execute(self):
        pass


if __name__ == '__main__':
    main = Main()
    main.execute()
