from utils.property_utils import PropertyUtils


class Main:
    """Main execution class of the system."""

    def __init__(self):
        self.__property_util = PropertyUtils()
        self.__core_key = self.__property_util.get_property('core_key')
        print(self.__core_key)

    def execute(self):
        self.__set_parameters_research()
        self.__download_json()
        self.__export_pdfs()

    def __set_parameters_research(self):
        pass

    def __download_json(self):
        pass

    def __export_pdfs(self):
        pass


if __name__ == '__main__':
    main = Main()
    main.execute()
