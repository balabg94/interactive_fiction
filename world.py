import json
import sys
def load_file(path):
    wrapper = open(path, "r+")
    data = wrapper.readline()
    global loaded_map
    loaded_map = json.loads(data)

load_file("./maps.json")
print(loaded_map)
