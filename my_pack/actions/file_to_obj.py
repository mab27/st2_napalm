import json
from st2actions.runners.pythonrunner import Action


class fileToObj(Action):
    def run(self, file_location, file_name, key):

        file_path = file_location + "inputs/" + file_name

        with open(file_path) as json_data:
            data_loaded = json.load(json_data)
            obj = data_loaded[key]

        result = dict.fromkeys([key])
        result[key] = obj

        return result


        """
        east_Router_Hostname = data_loaded["eastRouter"]["hostname"]
        east_Router_Id = data_loaded["eastRouter"]["routerId"]
        east_Local_ASN = data_loaded["eastRouter"]["localASN"]
        east_Peer_IP = data_loaded["eastRouter"]["peerIP"]

        west_Router_Hostname = data_loaded["westRouter"]["hostname"]
        west_Router_Id = data_loaded["westRouter"]["routerId"]
        west_Local_ASN = data_loaded["westRouter"]["localASN"]
        west_Peer_IP = data_loaded["westRouter"]["peerIP"]
        """

        # return result