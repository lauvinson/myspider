import requests as req
from requests import ReadTimeout, RequestException

try:
    def get(url, params=None, cookies=None, headers=None, timeout=30):
        r = req.get(url, params, headers=headers, cookies=cookies, timeout=timeout)
        r.encoding = r.apparent_encoding
        return r
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')
