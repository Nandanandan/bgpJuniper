#objective of this script is to verify the bgp peering after configuration.

import sys
from jnpr.junos import Device
from jnpr.junos import rpcmeta
from jnpr.junos.exception import RPCError,RpcTimeoutError
import yaml

inventory_file = 'hostfile.yaml'

with open(inventory_file) as data:
    inv = yaml.load(data)
    # Load the inventory file

    for node in inv['device']:
        try:
            dev = Device(host=node["ip"], user=node["username"], passwd=node["password"], port=node["port"]).open()
            #Login to the device suing SSH
            bgp_status = dev.rpc.get_bgp_summary_information({'format':'json'})
           #Intiate RPC call to nodes to retrieve BGP summry. Equivalant command "show bgp summary"
            print(f"\nBGP STATUS FOR {node['lo0']}\n")
            for peer in bgp_status['bgp-information'][0]['bgp-peer']:
                #Run through data and retrieve detaills for each peer
                print(f"Bgp Peer: {peer['peer-address'][0]['data']}  Status: {peer['peer-state'][0]['data']} Uptime: {peer['elapsed-time'][0]['data']}")

                # Expected output per node
                #
                # BGP STATUS FOR 10.100.100.1
                #
                # Bgp Peer: 10.100.100.2  Status: Established Uptime: 3:38:34
                # Bgp Peer: 10.100.100.3  Status: Connect Uptime: 3:38:56
                # Bgp Peer: 10.100.100.4  Status: Established Uptime: 3:38:14
            dev.close()
            # Close the SSH connection
        except RPCError as e:
            print(e)
        except RpcTimeoutError as f:
            print(f)
        except Exception as exp:
            print(exp)
