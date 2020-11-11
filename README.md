# bgp configuration in Juniper
----------------
Script is segmented into two parts

1. Configuration of iBGP between set of Juniper devices.
    * Jinja2 template(_bgpconfig.j2_) is used for generating configuration with inventory as _hostfile.yaml_
1. Verify bgp status and uptime post configuration.
    * Two scripts available, one works with Json and other with XML.
1. iBGP Configuration and status retrieval is done using SSH as transport.

# Steps:

1. Create a new directory
1. Create a virtual env with python3
`python3 -m venv .`
1. Clone the repo from Github.
`git clone https://github.com/Nandanandan/bgpJuniper.git`
1. Activate the venv
`source bin/activate`
1. Navigate to the directory(bgpJuniper) and Install the requirements
`pip install -r req.txt`
1. Edit the `hostfile.yaml` as per requirement
1. Initiate BGP configuration
`python vMX_config.py`
1. Verify bGP status
`python vMX_Bgp_status_xml.py`

   _Expected output format:_

    ```
    BGP STATUS FOR 10.100.100.1

    Bgp peer: 10.100.100.2     |  Status: Established     |  Uptime: 3:25:32
    Bgp peer: 10.100.100.3     |  Status: Active          |  Uptime: 3:25:54
    Bgp peer: 10.100.100.4     |  Status: Established     |  Uptime: 3:25:12
    ```
    OR

   `python vMX_Bgp_status_xml.py`
   
   _Expected output format:_


   ```
   BGP STATUS FOR 10.100.100.1

    Bgp Peer: 10.100.100.2  State: Established Uptime: 3:34:58
    Bgp Peer: 10.100.100.3  State: Active Uptime: 3:35:20
    Bgp Peer: 10.100.100.4  State: Established Uptime: 3:34:38

   ```

This script can be used to configure anything in juniper devices subject to input of proper Jinja2 template and respective inventory.
