import yaml
from st2actions.runners.pythonrunner import Action


class extract(Action):
    def run(self, eastRouter, westRouter):
      
        # Check that all required parameters are provided

        result = dict.fromkeys(['east_Router_Hostname','east_Router_Driver','east_Router_Id','east_Local_ASN','east_Peer_IP','west_Router_Hostname','west_Router_Driver','west_Router_Id','west_Local_ASN','west_Peer_IP'])

        try:
            east_Router_Hostname = eastRouter['hostname']
            result['east_Router_Hostname']=east_Router_Hostname
        except:
            return (False, "Missing hostname in eastRouter")

        try:
            east_Local_ASN = eastRouter['localASN']
            result['east_Local_ASN']=east_Local_ASN
        except:
            return (False, "Missing Local ASN in eastRouter")

        try:
            east_Router_Id = eastRouter['routerId']
            result['east_Router_Id']=east_Router_Id
        except:
            return (False, "Missing Router ID in eastRouter")

        try:
            east_Peer_IP = eastRouter['peerIP']
            result['east_Peer_IP']=east_Peer_IP
        except:
            return (False, "Missing Peer IP in eastRouter")

        try:
            west_Router_Hostname = westRouter['hostname']
            result['west_Router_Hostname']=west_Router_Hostname
        except:
            return (False, "Missing hostname in westRouter")

        try:
            west_Local_ASN = westRouter['localASN']
            result['west_Local_ASN']=west_Local_ASN
        except:
            return (False, "Missing Local ASN in westRouter")

        try:
            west_Router_Id = westRouter['routerId']
            result['west_Router_Id']=west_Router_Id
        except:
            return (False, "Missing Router ID in westRouter")

        try:
            west_Peer_IP = westRouter['peerIP']
            result['west_Peer_IP']=west_Peer_IP
        except:
            return (False, "Missing Peer IP in westRouter")

        # Open the NAPALM config file and extract the list of devices.
        ###################################################################

        # napalm.yaml file is a YAML dictionnary: keys are separated from values by a colon + space
        # There are 4 keys (html_table_class, config_repo, credentials and devices)
        # We are interested by the last key

        with open("/opt/stackstorm/configs/napalm.yaml", 'r') as napalm_config:
            data_loaded = yaml.load(napalm_config)

        devices = data_loaded["devices"]
        # the value for that last key is a list of lists

        # print devices
        hostname_list = list()
        driver_list = list()

        for device in devices:
            hostname = device["hostname"]
            driver = device["driver"]
            hostname_list.append(hostname)
            driver_list.append(driver)

        device_list = {}
        device_list = dict(zip(hostname_list, driver_list))

        print device_list

        # Check that all hostname routers exists in the NAPALM config file
        ###################################################################

        try:
            east_Router_Driver = device_list.get(east_Router_Hostname)
            result['east_Router_Driver']=east_Router_Driver
            # print east_Router_Driver
        except:
            return (False, "Missing entry for :" + east_Router_Hostname + "in the napalm.yaml file")

        try:
            west_Router_Driver = device_list.get(west_Router_Hostname)
            result['west_Router_Driver']=west_Router_Driver
            # print west_Router_Driver
        except:
            return (False, "Missing entry for :" + west_Router_Hostname + "in the napalm.yaml file")

        return result
