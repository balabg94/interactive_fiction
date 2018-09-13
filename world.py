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
        return out_str, current_room, '\n'
    elif out == 1:
        object_in_room = object_description(current_room)
        return loaded_map[current_room][0], current_room, object_in_room


def save_file(final_map):
    dumped_dictio = json.dumps(final_map)
    loaded_dictio = json.loads(dumped_dictio)
    
    with open('maps.json', 'w') as outfile:
        json.dump(loaded_dictio, outfile)
        
    outfile.close()
def object_description(current_player_pos):
    objects_in_current_pos = []
    for i in loaded_map['OBJECTS']:
        if loaded_map[i][0] == current_player_pos:
            objects_in_current_pos.append(loaded_map[i][1])
    objects_description = ' '.join(objects_in_current_pos)
    return objects_description.strip() + '\n'

def get_exits(current_room):
    exits_list = loaded_map[current_room][1:]
    exits_str = 'The exits are'
    for i in exits_list:
        exits_str = exits_str  +' '+ i[0]
    return exits_str
