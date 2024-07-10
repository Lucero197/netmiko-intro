from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# Datos de conexión de los routers
router1 = {
    'device_type': 'cisco_ios',
    'host': ' 10.0.0.69',
    'username': 'admin',
    'password': 'admin_password',
    'port': 22,
    'secret': '',  # si es necesario
}

router2 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.70',
    'username': 'admin',
    'password': 'admin_password',
    'port': 22,
    'secret': '',  # si es necesario
}

# Comandos de configuración para Router 1
config_commands_router1 = [
    'interface e0/0',
    'ip address dhcp',
    'no shutdown',
    'exit',
    'interface e0/2',
    'ip address 192.168.23.1 255.255.255.252',
    'no shutdown',
    'exit',
    'interface e0/3',
    'ip address 172.26.23.1 255.255.255.128',
    'no shutdown',
    'exit',
    'ip dhcp pool PC1_Pool',
    'network 172.26.23.0 255.255.255.128',
    'default-router 172.26.23.1',
    'exit',
    'ip nat inside source list 1 interface eth1 overload',
    'access-list 1 permit 172.26.23.0 0.0.0.127',
    'ip route 172.26.23.128 255.255.255.128 192.168.23.2',
    'line vty 0 4',
    'transport input ssh',
    'login local',
    'exit',
    'ip domain-name example.com',
    'crypto key generate rsa modulus 1024',
    'username admin privilege 15 secret admin_password',
]

# Comandos de configuración para Router 2
config_commands_router2 = [
    'interface e0/0',
    'ip address dhcp',
    'no shutdown',
    'exit',
    'interface e0/2',
    'ip address 192.168.23.2 255.255.255.252',
    'no shutdown',
    'exit',
    'interface e0/3',
    'ip address 172.26.23.129 255.255.255.128',
    'no shutdown',
    'exit',
    'ip dhcp pool PC2_Pool',
    'network 172.26.23.128 255.255.255.128',
    'default-router 172.26.23.129',
    'exit',
    'ip nat inside source list 1 interface eth1 overload',
    'access-list 1 permit 172.26.23.128 0.0.0.127',
    'ip route 172.26.23.0 255.255.255.128 192.168.23.1',
    'line vty 0 4',
    'transport input ssh',
    'login local',
    'exit',
    'ip domain-name example.com',
    'crypto key generate rsa modulus 1024',
    'username admin privilege 15 secret admin_password',
]

try:
    # Conexión y configuración de Router 1
    conexion1 = ConnectHandler(**router1)
    output1 = conexion1.send_config_set(config_commands_router1)
    print(output1)
    conexion1.disconnect()
except NetmikoTimeoutException:
    print("Timeout al intentar conectar con el Router 1")
except NetmikoAuthenticationException:
    print("Error de autenticación al intentar conectar con el Router 1")
except Exception as e:
    print(f"Error desconocido al intentar conectar con el Router 1: {e}")

try:
    # Conexión y configuración de Router 2
    conexion2 = ConnectHandler(**router2)
    output2 = conexion2.send_config_set(config_commands_router2)
    print(output2)
    conexion2.disconnect()
except NetmikoTimeoutException:
    print("Timeout al intentar conectar con el Router 2")
except NetmikoAuthenticationException:
    print("Error de autenticación al intentar conectar con el Router 2")
except Exception as e:
    print(f"Error desconocido al intentar conectar con el Router 2: {e}")