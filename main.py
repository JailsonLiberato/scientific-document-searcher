from core_api_requestor import CoreApiRequestor
from utils.property_utils import PropertyUtils


class Main:
    """Main execution class of the system."""

    def __init__(self):
        self.__property_util = PropertyUtils()
        self.__core_key = self.__property_util.get_property('core_key')
        self.__endpoint = self.__property_util.get_property('end_point')
        self.__api = CoreApiRequestor(self.__endpoint, self.__core_key)
        self.__method = self.__property_util.get_property('method')
        self.__query = self.__property_util.get_property('query')

    def execute(self):
        self.__download_json()
        self.__export_pdfs()

    def __download_json(self):
        test = self.__api.get_method_query_request_url(self.__method, self.__query, False, 1)
        print(test)

    def __export_pdfs(self):
        pass


if __name__ == '__main__':
    main = Main()
    main.execute()
