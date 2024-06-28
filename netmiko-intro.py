from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.26',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
    '/ip service enable ssh',
    '/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade',
    '/ip address add address=172.25.23.1/25 interface=ether2',
    '/ip dns set servers=8.8.8.8,8.8.4.4',
    '/ip pool add name=dhcp_pool ranges=172.25.23.130-172.25.23.254',
    '/ip dhcp-server add address-pool=dhcp_pool interface=ether3 name=dhcp1',
    '/ip dhcp-server network add address=172.25.23.128/25 gateway=172.25.23.129',
    '/export file=archivo',
    '/system reset-configuration no-default=yes skip-backup=yes',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()