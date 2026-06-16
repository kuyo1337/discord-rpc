import json
import ssl
import http.client
from urllib.parse import urlparse


class reqresp:
    def __init__(self, status, data):
        self.status_code = status
        self._data = data

    @property
    def text(self):
        return self._data.decode("utf-8", errors="ignore")

    def json(self):
        try:
            return json.loads(self._data.decode("utf-8"))
        except:
            return None


class requesters:
    @staticmethod
    def request(method, url, headers=None, json_data=None):
        headers = headers or {}
        parsed = urlparse(url)

        conn = (
            http.client.HTTPSConnection(parsed.netloc, context=ssl.create_default_context())
            if parsed.scheme == "https"
            else http.client.HTTPConnection(parsed.netloc)
        )

        body = json.dumps(json_data) if json_data else None

        conn.request(method, parsed.path or "/", body=body, headers=headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()

        return reqresp(res.status, data)

    @staticmethod
    def get(url, headers=None):
        return requesters.request("GET", url, headers)

    @staticmethod
    def post(url, headers=None, json_data=None):
        return requesters.request("POST", url, headers, json_data)
