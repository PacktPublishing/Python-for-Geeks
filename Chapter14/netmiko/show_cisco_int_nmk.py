from netmiko import ConnectHandler

cisco_rtr = {
    "device_type": "cisco_ios",
    "host": "172.16.2.34",
    "username": "root",
    "password": "xxxxx",
}

def main():
    command = "show ip int brief"
    with ConnectHandler(**cisco_rtr) as net_connect:
        print(net_connect.find_prompt())
        print(net_connect.enable())
        output = net_connect.send_command(command)

    print(output)

if __name__ == '__main__':
    main()
