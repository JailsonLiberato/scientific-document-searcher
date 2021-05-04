from urllib.error import HTTPError
from scihub import SciHub, DocumentUrlNotFound
from core_api_requestor import CoreApiRequestor
from utils.property_utils import PropertyUtils
import json
import os


class Main:
    """Main execution class of the system."""

    def __init__(self):
        self.__property_util = PropertyUtils()
        self.__core_key = self.__property_util.get_property('core_key')
        self.__endpoint = self.__property_util.get_property('end_point')
        self.__api = CoreApiRequestor(self.__endpoint, self.__core_key)
        self.__method = self.__property_util.get_property('method')
        self.__query = self.__property_util.get_property('query')
        self.__page_size = self.__property_util.get_property('page_size')
        self.__num_of_pages = 0
        self.__total_records = 0
        self.__results = []

    def execute(self):
        self.__prepare_statement()
        self.__download_json()
        self.__export_pdfs()

    def __prepare_statement(self):
        url = self.__api.get_method_query_request_url(self.__method, self.__query, False, 1)
        result = CoreApiRequestor.request_url(url)
        result = json.loads(result)
        self.__total_records = result["totalHits"]
        self.__num_of_pages = int(self.__total_records / int(self.__page_size))

    def __download_json(self):
        for page in range(self.__num_of_pages):
            page += 1
            self.__load_page(page)
            print(page)
        print(self.__results)

    def __load_page(self, page: int):
        try:
            url = self.__api.get_method_query_request_url(self.__method, self.__query, False, page)
            result = CoreApiRequestor.request_url(url)
            result = json.loads(result)
            self.__export_pdfs(result)
            self.__results.append(result)
        except HTTPError as exception:
            print("Error ", page)
            print(exception)

    def __export_pdfs(self, result):
        for r in result['data']:
            full_text_identifier = r['_source']['fullTextIdentifier']
            if full_text_identifier:
                self.__export_pdf(full_text_identifier, r['_source']['title'])

    def __export_pdf(self, url, title):
        try:
            sh = SciHub()
            result = sh.fetch(url)

            title = 'articles/' + title
            with open(title + '.pdf', 'wb+') as fd:
                fd.write(result['pdf'])
        except DocumentUrlNotFound as documentNotFount:
            print(documentNotFount)
        except Exception as exception:
            print('Problem!')


if __name__ == '__main__':
    main = Main()
    main.execute()
