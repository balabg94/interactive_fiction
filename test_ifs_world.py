import pytest
import world

def test_loads_file():
    # tests if the map is loaded into a variable.
    assert world.load_file("./maps.json") == {"0": ["You are standing at the end of a corridor. There is a door in front of you.", ["S", "1"]], "1": ["You are standing in what seems to be a living room.", ["E", "2"], ["N", "0"]], "2": ["You are standing in what seems to be a hall way connecting many room.", ["W", "1"], ["N", "3"], ["E", "5"], ["S", "6"]], "3": ["Your are standing in what seems to be a bedroom. It has got a balcony attached.", ["E", "4"], ["S", "2"]], "4": ["You are standing in the balcony of Room number 3.", ["W", "3"]], "5": ["You are standing in the balcony attached to the hallway.", ["W", "2"]], "6": ["You are standing in a connecting hallway. Three doors await you.", ["N", "2"], ["S", "9"], ["E", "7"], ["W", "8"]], "7": ["You are standing in a kitchen. Utensils everywhere.", ["W", "6"]], "8": ["You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.", ["E", "6"], ["S", "10"]], "9": ["You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.", ["N", "6"], ["S", "11"]], "10": ["You are standing in the balcony of room number 8.", ["N", "8"]], "11": ["You are standing in the balcony of room number 9.", ["N", "9"]]}

def test_start_position():
    # tesrs if the start position returns the description of the zeroth room

    assert world.start_postion() == "You are standing at the end of a corridor. There is a door in front of you."
