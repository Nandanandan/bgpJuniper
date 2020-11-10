#objective of this script is to verify the bgp peering after configuration.

import sys
from jnpr.junos import Device
from jnpr.junos import rpcmeta
from jnpr.junos.exception import RPCError,RpcTimeoutError
import yaml

inventory_file = 'hostfile.yaml'
#filter = '<bgp-information><bgp-peer><peer-address><peer-address/><bgp-peer/><bgp-information/>'

with open(inventory_file) as data:
    inv = yaml.load(data)

    for node in inv['device']:
        try:
            dev = Device(host=node["ip"], user=node["username"], passwd=node["password"], port=node["port"]).open()
            bgp_status = dev.rpc.get_bgp_summary_information({'format':'json'})
            print(f"\nBGP STATUS FOR {node['lo0']}\n")
            for peer in bgp_status['bgp-information'][0]['bgp-peer']:
                print(f"Bgp Peer: {peer['peer-address'][0]['data']}  State: {peer['peer-state'][0]['data']} Uptime: {peer['elapsed-time'][0]['data']}")
        except RPCError as e:
            print(e)
        except RpcTimeoutError as f:
            print(f)
        except Exception as exp:
            print(exp)
