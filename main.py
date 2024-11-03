# main.py

from zabbix_host import ZabbixHost
from zabbix_item import ZabbixItem

def main():
    # Gather initial Zabbix connection information
    print("Welcome to the Zabbix API Tool")
    zabbix_url = input("Enter the Zabbix URL (e.g., http://your-zabbix-server-url/zabbix/api_jsonrpc.php): ")
    api_token = input("Enter your API Token: ")

    # Initialize the Zabbix client classes
    host_client = ZabbixHost(zabbix_url, api_token)
    item_client = ZabbixItem(zabbix_url, api_token)

    while True:
        # Display the menu options
        print("\nPlease choose an option:")
        print("1. List Hosts")
        print("2. List Items for a Host")
        print("3. Exit")

        # Get user choice
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # List all hosts
            try:
                hosts = host_client.get_hosts()
                print("\nHost List:")
                for host in hosts:
                    print(f"ID: {host['hostid']}, Name: {host['host']}")
            except Exception as e:
                print(f"Error retrieving hosts: {e}")

        elif choice == '2':
            # List items for a specific host
            host_id = input("Enter the Host ID to retrieve items: ")
            try:
                items = item_client.get_items(host_id)
                print("\nItems List:")
                for item in items:
                    print(f"ID: {item['itemid']}, Name: {item['name']}")
            except Exception as e:
                print(f"Error retrieving items for host {host_id}: {e}")

        elif choice == '3':
            # Exit the program
            print("Exiting the Zabbix API Tool.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
