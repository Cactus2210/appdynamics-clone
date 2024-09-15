import requests
from time import time

def get_api_status():
    api_urls = ['https://example-api.com']
    status = {}

    for url in api_urls:
        start = time()
        try:
            response = requests.get(url)
            latency = time() - start
            status[url] = {
                'latency': latency,
                'status_code': response.status_code
            }
        except Exception as e:
            status[url] = {
                'error': str(e)
            }
    
    return status
