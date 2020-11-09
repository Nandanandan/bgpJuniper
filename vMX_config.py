import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
import yaml


# class bgp:
#
#     def __init__(self):
#         self.host = host
#         self.uname = uname
#         self.passwd = passwd
#         self.port = port
#
#     def bgpConfig(self):
#

template_file = 'bgpconfig.j2'
inventory_file = 'hostfile.yaml'

with open(inventory_file) as data:
    inv = yaml.load(data)

    for node in inv['device']:
        try:
            dev = Device(host=node["ip"], user=node["username"], passwd=node["password"], port=node["port"]).open()
            with Config(dev, mode="private") as jp:
                jp.load(template_path=template_file, template_vars=node, format='set')
                jp.pdiff()
                jp.commit()
            dev.close()
        except ValueError as e:
            print(e)
