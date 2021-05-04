import json
import urllib.parse
import urllib.request


class CoreApiRequestor:
    """API to search for articles."""

    def __init__(self, endpoint, api_key, page_size=100, page=1):
        self.endpoint = endpoint
        self.api_key = api_key
        self.pagesize = page_size
        self.page = page

    @staticmethod
    def parse_response(decoded):
        res = []
        for item in decoded['data']:
            doi = None
            if 'identifiers' in item:
                for identifier in item['identifiers']:
                    if identifier and identifier.startswith('doi:'):
                        doi = identifier
                        break
            res.append([item['title'], doi])
        return res

    @staticmethod
    def request_url(url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
        return html

    def get_method_query_request_url(self, method, query, fullText, page, page_size=100):
        if (fullText):
            fullText = 'true'
        else:
            fullText = 'false'
        params = {
            'apiKey': self.api_key,
            'page': page,
            'pageSize': page_size,
            'fulltext': fullText
        }
        return self.endpoint + method + '/' + urllib.parse.quote(query) + '?' + urllib.parse.urlencode(params)

    def get_up_to_20_pages_of_query(self, method, query, fulltext):
        url = self.get_method_query_request_url(method, query, fulltext, 1)
        all_articles = []
        resp = self.request_url(url)
        result = json.loads(resp.decode('utf-8'))
        all_articles.append(result)
        if result['totalHits'] > 100:
            numOfPages = int(result['totalHits'] / self.pagesize)  # rounds down
            if numOfPages > 20:
                numOfPages = 20
            for i in range(2, numOfPages):
                url = self.get_method_query_request_url(method, query, False, i)
                print(url)
                resp = self.request_url(url)
                all_articles.append(json.loads(resp.decode('utf-8')))
        return all_articles
