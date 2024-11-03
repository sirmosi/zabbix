# zabbix_client.py

import requests
import json

class ZabbixClient:
    def __init__(self, url, api_token):
        self.url = url
        self.api_token = api_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'
        }

    def request(self, method, params):
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1,
        }
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        result = response.json()
        if 'error' in result:
            raise Exception(f"API Error: {result['error']}")
        return result['result']
