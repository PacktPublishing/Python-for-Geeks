from napalm import get_network_driver
import json

def main():

    driver = get_network_driver('iosxr')
    device = driver('172.16.2.50', 'root', 'rootroot')
    try:
        device.open()
        device.load_merge_candidate(config='interface Lo0 \n description napalm added new desc \n end\n')
        print(device.compare_config())
        device.commit_config()
    finally:
        device.close()

if __name__ == '__main__':
    main()
