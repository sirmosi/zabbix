# Zabbix Python Client

This repository provides a Python client for interacting with the Zabbix API, facilitating the automation of monitoring tasks and the integration of Zabbix functionalities into Python applications.

---

## Features

- **ZabbixClient Class**: Manages API requests to the Zabbix server.
- **ZabbixHost Class**: Handles operations related to Zabbix hosts.
- **ZabbixItem Class**: Manages Zabbix items for monitoring.

---

## Installation

1. **Clone the Repository**:
```bash
   git clone https://github.com/sirmosi/zabbix.git
```

## Navigate to the Project Directory:

```
cd zabbix
```

Install Dependencies:

```python
    pip install -r requirements.txt
```
    Note: Ensure you have Python 3.x and pip installed.

Usage
```
    Import the Client:

from zabbix_client import ZabbixClient
```
Initialize the Client:
```
zabbix = ZabbixClient(url='http://your-zabbix-server/api_jsonrpc.php', api_token='your_api_token')

Make API Requests:

    response = zabbix.request(method='host.get', params={'output': 'extend'})
    print(response)
```
Project Structure

    main.py: Entry point for the application.
    zabbix_client.py: Contains the ZabbixClient class for API interactions.
    zabbix_host.py: Defines the ZabbixHost class for host-related operations.
    zabbix_item.py: Defines the ZabbixItem class for item-related operations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For questions or suggestions, please open an issue on GitHub.

**Note**: This project is under development. Features and documentation are subject to change.