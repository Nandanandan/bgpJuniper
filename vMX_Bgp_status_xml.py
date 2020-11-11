#objective of this script is to verify the bgp peering after configuration.

import sys
from jnpr.junos import Device
from jnpr.junos import rpcmeta
from jnpr.junos.exception import RPCError,RpcTimeoutError
import yaml
from lxml import etree

inventory_file = 'hostfile.yaml'

with open(inventory_file) as data:
    inv = yaml.load(data)
# Load the inventory file

    for node in inv['device']:
        try:
            dev = Device(host=node["ip"], user=node["username"], passwd=node["password"], port=node["port"]).open()
            #Login to the device suing SSH
            bgp_status = dev.rpc.get_bgp_summary_information(normalize=True)
            #Intiate RPC call to nodes to retrieve BGP summry. Equivalant command "show bgp summary"
            peers = bgp_status.findall('.//bgp-peer')
            #Find all the peers available under List bgp-peer
            print(f"\nBGP STATUS FOR {node['lo0']}\n")
            for peer in peers:
                #Run through data and retrieve detaills for each peer
                print(f"Bgp peer: {peer.findtext('peer-address'):15}  |  Status: {peer.findtext('peer-state'):15} |  Uptime: {peer.findtext('elapsed-time'):15} ")

                # Expected output per node
                #
                # BGP STATUS FOR 10.100.100.1
                #
                # Bgp peer: 10.100.100.2     |  Status: Established     |  Uptime: 3:25:32
                # Bgp peer: 10.100.100.3     |  Status: Active          |  Uptime: 3:25:54
                # Bgp peer: 10.100.100.4     |  Status: Established     |  Uptime: 3:25:12
            dev.close()
            # Close the SSH connection
        except RPCError as e:
            print(e)
        except RpcTimeoutError as f:
            print(f)
        except Exception as exp:
            print(exp)
