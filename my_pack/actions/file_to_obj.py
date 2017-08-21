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
