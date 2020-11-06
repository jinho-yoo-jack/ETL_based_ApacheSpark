from elasticsearch import Elasticsearch
import json


class SearchEngine:

    def __init__(self, esEndpoint: list, queryOptions):
        try:
            if esEndpoint is not None:
                self.es: Elasticsearch = Elasticsearch(hosts=esEndpoint)
                self.prevIdx = None
                self.prevDocCnt = 0
            else:
                Exception
        except Exception as e:
            print(e)

    def insertMapping(self):
        if self.es.indices.exists(index='lst_test'):
            pass
        else:
            # 1. Mapping File Search
            with open('/Users/jinokku/PycharmProjects/pythonProject/mapping/mapping.json', 'r') as f:
                # 2. Read File And Parsing
                mapping = json.load(f)
            # 3. Call ES API '_mapping'
            resp = self.es.indices.create(index="list_test", body=mapping)
            # 4. Check Result


    def getPrevIdxDocCnt(self):
        # 1. Call ES API '_cat/indices/INDEX_NAME'
        # 2. SET Last INDEX_NAME 'doc.count' at self.prevIdx = None
        pass

    def getPrevIdxAlias(self):
        pass


if __name__ == '__main__':
    esAddr: list = ['localhost:9200']

    elastic: SearchEngine = SearchEngine(esAddr)
    es: Elasticsearch = elastic.es
    elastic.insertMapping()
