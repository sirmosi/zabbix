# zabbix_host.py

from zabbix_client import ZabbixClient

class ZabbixHost(ZabbixClient):
    def get_hosts(self):
        return self.request("host.get", {"output": ["hostid", "host"]})
