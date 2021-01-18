from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

devices = [
{
'device_type': 'cisco_ios',
'ip': 'ios-xe-mgmt.cisco.com',
'username': 'developer',
'password': 'C1sco12345'
},
]

for all_devices in devices:
    try:
        connection = ConnectHandler(**all_devices)
    except Exception as unknown_error:
        print ('Error no identificado segun captura en el log es: \n ' + str(unknown_error))
    show_ver = connection.send_command('show ver')
    print (show_ver)
    print ("#"*100)
    comando2 = connection.send_command('show ip int brief ')
    print ("Interfaces in raw text (cli) format")
    print (comando2)
    print ("#"*100)
    print ("Extraer  todas las  interfaces ")
    for x in comando2.splitlines():
        if not 'Interface' in x:
           print (x.split()[0])
    print ("#"*100)