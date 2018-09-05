import json
import sys
def load_file(path):
    wrapper = open(path, "r+")
    data = wrapper.readline()
    global loaded_map
    loaded_map = json.loads(data)
    return loaded_map

def start_position():
    global start_pos
    start_pos = loaded_map["0"][0]
    return start_pos

