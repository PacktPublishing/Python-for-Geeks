from netmiko import ConnectHandler

cisco_rtr = {
    "device_type": "cisco_ios",
    "host": "172.16.2.34",
    "username": "root",
    "password": "xxxx",
}

def main():
    commands = ["int Lo0", "description my custom description", "commit"]
    # commands =["logging buffered 100000"]
    with ConnectHandler(**cisco_rtr) as net_connect:
        output = net_connect.send_config_set(commands)

    print(output)
    print()

if __name__ == '__main__':
    main()
