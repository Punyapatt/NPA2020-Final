from netmiko import ConnectHandler
import time

device_ip = '10.0.15.109'
username = 'admin'
password = 'cisco'
config_command = ['en', 'int lo61070122', 'ip add 192.168.1.1 255.255.255.0', 'no shut', 'end', 'sh ip int b']
device_params = {'device_type': 'cisco_ios',
                 'ip': device_ip,
                 'username': username,
                  'password': password,
                }

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_config_set(config_command)
    print(result)