# zabbix_item.py

from zabbix_client import ZabbixClient

class ZabbixItem(ZabbixClient):
    def get_items(self, host_id):
        return self.request("item.get", {"hostids": host_id, "output": ["itemid", "name"]})
