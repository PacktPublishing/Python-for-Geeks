from napalm import get_network_driver
import json

def main():
    driver = get_network_driver('iosxr')
    device = driver('172.16.2.50', 'root', 'rootroot')

    try:
        device.open()
        print(json.dumps(device.get_interfaces_ip(), indent=2))
        print(json.dumps(device.get_facts(), indent=2))

    finally:
        device.close()

if __name__ == '__main__':
    main()
