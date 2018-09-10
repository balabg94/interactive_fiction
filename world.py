import json
import sys
def load_file():
    wrapper = open("./maps.json", "r+")
    data = wrapper.readline()
    global loaded_map
    loaded_map = json.loads(data)
    return loaded_map

def start_position():
    global start_pos
    start_pos = loaded_map["0"][0]
    return start_pos

def if_exit(current_room, out_path):
    out = 0
    out_str = "No exit that way"
    for i in loaded_map[current_room][1:]:
        if out_path not in i:
            #print(len(loaded_map[current_room]))
            #print(loaded_map[current_room][i])
            out = 0
            
        elif out_path in i:
            #print(loaded_map[current_room][i][1])
            current_room = i[1]
            loaded_map["PLAYER"] = current_room
            out = 1
            break
        else:
            return "ERROR"
    if out == 0:
        return out_str, current_room
    elif out == 1:
        return loaded_map[current_room][0], current_room


def save_file(final_map):
    dumped_dictio = json.dumps(final_map)
    loaded_dictio = json.loads(dumped_dictio)
    
    with open('maps.json', 'w') as outfile:
        json.dump(loaded_dictio, outfile)
        
    outfile.close()
