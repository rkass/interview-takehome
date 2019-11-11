from functools import lru_cache

import elasticsearch

ES_HOST = 'elasticsearch:9200'
INDEX_NAME = 'wikis'

INDEX_BODY = {
    "settings": {
      "index": {
        "number_of_shards": 8,
        "number_of_replicas": 1
        }
    },
    "mappings": {
      "_meta": {
        "index_type": "wikis",
        "version": "1.0",
      },
      "_source": {
        "enabled": True
      },
      "properties": {
        "id": {
          "type": "keyword"
        },
        "link": {
          "type": "keyword"
        },
        "title": {
          "type": "text",
        },
        "contents": {
          "type": "text"
        }
      }
    }
  }


@lru_cache()
def _client_for_host(host):
    return elasticsearch.Elasticsearch(host)


@lru_cache()
def _indices_client_for_host(host):
    return elasticsearch.client.IndicesClient(_client_for_host(host))


def load_data():
    pass


def create_index():
    _indices_client_for_host(ES_HOST).create(INDEX_NAME, body=INDEX_BODY)
