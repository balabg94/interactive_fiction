import pytest
import world
import json




def test_loads_file():
    # tests if the map is loaded into a variable.
    assert world.load_file() == {"PLAYER": "0", "Vase": ["1", "There is a blue vase in the room."], "Knife": ["7", "You can see a knife in front of you."], "Ball": ["5", "There is a red tennis ball in front of you."], "0": ["You are standing at the end of a corridor. There is a door in front of you.", ["S", "1"]], "1": ["You are standing in what seems to be a living room.", ["E", "2"], ["N", "0"]], "2": ["You are standing in what seems to be a hall way connecting many room.", ["W", "1"], ["N", "3"], ["E", "5"], ["S", "6"]], "3": ["Your are standing in what seems to be a bedroom. It has got a balcony attached.", ["E", "4"], ["S", "2"]], "4": ["You are standing in the balcony of Room number 3.", ["W", "3"]], "5": ["You are standing in the balcony attached to the hallway.", ["W", "2"]], "6": ["You are standing in a connecting hallway. Three doors await you.", ["N", "2"], ["S", "9"], ["E", "7"], ["W", "8"]], "7": ["You are standing in a kitchen. Utensils everywhere.", ["W", "6"]], "8": ["You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.", ["E", "6"], ["S", "10"]], "9": ["You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.", ["N", "6"], ["S", "11"]], "10": ["You are standing in the balcony of room number 8.", ["N", "8"]], "11": ["You are standing in the balcony of room number 9.", ["N", "9"]]}

def test_start_position():
    # tesrs if the start position returns the description of the zeroth room
    assert world.start_position() == "You are standing at the end of a corridor. There is a door in front of you."

    
# Zeroth Room
    
def test_wrong_exit_0_1():
    # to test the output in case of no exit
    assert world.if_exit("0", "N") == ("No exit that way", "0")

def test_wrong_exit_0_2():
    # to test the output in case of no exit
    assert world.if_exit("0", "E") == ("No exit that way", "0")

def test_wrong_exit_0_3():
    # to test the output in case of no exit
    assert world.if_exit("0", "W") == ("No exit that way", "0")

def test_correct_exit_0_4():
    # to test in case of correct exit
    assert world.if_exit("0", "S") == ("You are standing in what seems to be a living room.", '1')

    
# First Room

def test_wrong_exit_1_1():
    # to test the output in case of no exit
    assert world.if_exit("1", "W") == ("No exit that way", "1")

def test_wrong_exit_1_2():
    # to test the output in case of no exit
    assert world.if_exit("1", "S") == ("No exit that way", "1")

def test_correct_exit_1_3():
    # to test in case of correct exit
    assert world.if_exit("1", "E") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_1_4():
    # to test in case of correct exit
    assert world.if_exit("1", "N") == ("You are standing at the end of a corridor. There is a door in front of you.", '0')


# Room number 2
    
def test_correct_exit_2_1():
    # to test in case of correct exit
    assert world.if_exit("2", "S") == ('You are standing in a connecting hallway. Three doors await you.', '6')

def test_correct_exit_2_2():
    # to test in case of correct exit
    assert world.if_exit("2", "N") == ('Your are standing in what seems to be a bedroom. It has got a balcony attached.', '3')

def test_correct_exit_2_3():
    # to test in case of correct exit
    assert world.if_exit("2", "E") == ('You are standing in the balcony attached to the hallway.', '5')

def test_correct_exit_2_4():
    # to test in case of correct exit
    assert world.if_exit("2", "W") == ('You are standing in what seems to be a living room.', '1')

    
# Third Room    

def test_wrong_exit_3_1():
    # to test the output in case of no exit
    assert world.if_exit("3", "N") == ("No exit that way", "3")

def test_wrong_exit_3_2():
    # to test the output in case of no exit
    assert world.if_exit("3", "W") == ("No exit that way", "3")

def test_correct_exit_3_3():
    # to test in case of correct exit
    assert world.if_exit("3", "S") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_3_4():
    # to test in case of correct exit
    assert world.if_exit("3", "E") == ('You are standing in the balcony of Room number 3.', '4')

    
# Forth Room

def test_wrong_exit_4_1():
    # to test the output in case of no exit
    assert world.if_exit("4", "N") == ("No exit that way", "4")
    
def test_wrong_exit_4_2():
    # to test the output in case of no exit
    assert world.if_exit("4", "E") == ("No exit that way", "4")

def test_wrong_exit_4_3():
    # to test the output in case of no exit
    assert world.if_exit("4", "S") == ("No exit that way", "4")

def test_correct_exit_4_4():
    # to test in case of correct exit
    assert world.if_exit("4", "W") == ('Your are standing in what seems to be a bedroom. It has got a balcony attached.', '3')

    
# Fifth Room

def test_wrong_exit_5_1():
    # to test the output in case of no exit
    assert world.if_exit("5", "N") == ("No exit that way", "5")
    
def test_wrong_exit_5_2():
    # to test the output in case of no exit
    assert world.if_exit("5", "E") == ("No exit that way", "5")

def test_wrong_exit_5_3():
    # to test the output in case of no exit
    assert world.if_exit("5", "S") == ("No exit that way", "5")

def test_correct_exit_5_4():
    # to test in case of correct exit
    assert world.if_exit("5", "W") == ('You are standing in what seems to be a hall way connecting many room.', '2')

    
# Sixth Room
    
def test_correct_exit_6_1():
    # to test in case of correct exit
    assert world.if_exit("6", "S") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.', '9')

def test_correct_exit_6_2():
    # to test in case of correct exit
    assert world.if_exit("6", "N") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_6_3():
    # to test in case of correct exit
    assert world.if_exit("6", "E") == ('You are standing in a kitchen. Utensils everywhere.', '7')

def test_correct_exit_6_4():
    # to test in case of correct exit
    assert world.if_exit("6", "W") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.', '8')



# Seventh Room

def test_wrong_exit_7_1():
    # to test the output in case of no exit
    assert world.if_exit("7", "N") == ("No exit that way", "7")
    
def test_wrong_exit_7_2():
    # to test the output in case of no exit
    assert world.if_exit("7", "E") == ("No exit that way", "7")

def test_wrong_exit_7_3():
    # to test the output in case of no exit
    assert world.if_exit("7", "S") == ("No exit that way", "7")

def test_correct_exit_7_4():
    # to test in case of correct exit
    assert world.if_exit("7", "W") == ('You are standing in a connecting hallway. Three doors await you.', '6')


    
# Eigth Room

def test_wrong_exit_8_1():
    # to test the output in case of no exit
    assert world.if_exit("8", "N") == ("No exit that way", "8")

def test_wrong_exit_8_2():
    # to test the output in case of no exit
    assert world.if_exit("8", "W") == ("No exit that way", "8")

def test_correct_exit_8_3():
    # to test in case of correct exit
    assert world.if_exit("8", "S") == ('You are standing in the balcony of room number 8.', '10')

def test_correct_exit_8_4():
    # to test in case of correct exit
    assert world.if_exit("8", "E") == ('You are standing in a connecting hallway. Three doors await you.', '6')


# Ninth Room

def test_wrong_exit_9_1():
    # to test the output in case of no exit
    assert world.if_exit("9", "E") == ("No exit that way", "9")

def test_wrong_exit_9_2():
    # to test the output in case of no exit
    assert world.if_exit("9", "W") == ("No exit that way", "9")

def test_correct_exit_9_3():
    # to test in case of correct exit
    assert world.if_exit("9", "N") == ('You are standing in a connecting hallway. Three doors await you.', '6')

def test_correct_exit_9_4():
    # to test in case of correct exit
    assert world.if_exit("9", "S") == ('You are standing in the balcony of room number 9.', '11')

# Tenth Room

def test_wrong_exit_10_1():
    # to test the output in case of no exit
    assert world.if_exit("10", "W") == ("No exit that way", "10")
    
def test_wrong_exit_10_2():
    # to test the output in case of no exit
    assert world.if_exit("10", "E") == ("No exit that way", "10")

def test_wrong_exit_10_3():
    # to test the output in case of no exit
    assert world.if_exit("10", "S") == ("No exit that way", "10")

def test_correct_exit_10_4():
    # to test in case of correct exit
    assert world.if_exit("10", "N") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.', '8')

# Eleventh Room

def test_wrong_exit_11_1():
    # to test the output in case of no exit
    assert world.if_exit("11", "W") == ("No exit that way", "11")
    
def test_wrong_exit_11_2():
    # to test the output in case of no exit
    assert world.if_exit("11", "E") == ("No exit that way", "11")

def test_wrong_exit_11_3():
    # to test the output in case of no exit
    assert world.if_exit("11", "S") == ("No exit that way", "11")

def test_correct_exit_11_4():
    # to test in case of correct exit
    assert world.if_exit("11", "N") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.', '9')

    
# Zeroth Room
    
def test_wrong_exit_0_1():
    # to test the output in case of no exit
    assert world.if_exit("0", "N") == ("No exit that way", "0")

def test_wrong_exit_0_2():
    # to test the output in case of no exit
    assert world.if_exit("0", "E") == ("No exit that way", "0")

def test_wrong_exit_0_3():
    # to test the output in case of no exit
    assert world.if_exit("0", "W") == ("No exit that way", "0")

def test_correct_exit_0_4():
    # to test in case of correct exit
    assert world.if_exit("0", "S") == ("You are standing in what seems to be a living room.", '1')

    
# First Room

def test_wrong_exit_1_1():
    # to test the output in case of no exit
    assert world.if_exit("1", "W") == ("No exit that way", "1")

def test_wrong_exit_1_2():
    # to test the output in case of no exit
    assert world.if_exit("1", "S") == ("No exit that way", "1")

def test_correct_exit_1_3():
    # to test in case of correct exit
    assert world.if_exit("1", "E") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_1_4():
    # to test in case of correct exit
    assert world.if_exit("1", "N") == ("You are standing at the end of a corridor. There is a door in front of you.", '0')


# Room number 2
    
def test_correct_exit_2_1():
    # to test in case of correct exit
    assert world.if_exit("2", "S") == ('You are standing in a connecting hallway. Three doors await you.', '6')

def test_correct_exit_2_2():
    # to test in case of correct exit
    assert world.if_exit("2", "N") == ('Your are standing in what seems to be a bedroom. It has got a balcony attached.', '3')

def test_correct_exit_2_3():
    # to test in case of correct exit
    assert world.if_exit("2", "E") == ('You are standing in the balcony attached to the hallway.', '5')

def test_correct_exit_2_4():
    # to test in case of correct exit
    assert world.if_exit("2", "W") == ('You are standing in what seems to be a living room.', '1')

    
# Third Room    

def test_wrong_exit_3_1():
    # to test the output in case of no exit
    assert world.if_exit("3", "N") == ("No exit that way", "3")

def test_wrong_exit_3_2():
    # to test the output in case of no exit
    assert world.if_exit("3", "W") == ("No exit that way", "3")

def test_correct_exit_3_3():
    # to test in case of correct exit
    assert world.if_exit("3", "S") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_3_4():
    # to test in case of correct exit
    assert world.if_exit("3", "E") == ('You are standing in the balcony of Room number 3.', '4')

    
# Forth Room

def test_wrong_exit_4_1():
    # to test the output in case of no exit
    assert world.if_exit("4", "N") == ("No exit that way", "4")
    
def test_wrong_exit_4_2():
    # to test the output in case of no exit
    assert world.if_exit("4", "E") == ("No exit that way", "4")

def test_wrong_exit_4_3():
    # to test the output in case of no exit
    assert world.if_exit("4", "S") == ("No exit that way", "4")

def test_correct_exit_4_4():
    # to test in case of correct exit
    assert world.if_exit("4", "W") == ('Your are standing in what seems to be a bedroom. It has got a balcony attached.', '3')

    
# Fifth Room

def test_wrong_exit_5_1():
    # to test the output in case of no exit
    assert world.if_exit("5", "N") == ("No exit that way", "5")
    
def test_wrong_exit_5_2():
    # to test the output in case of no exit
    assert world.if_exit("5", "E") == ("No exit that way", "5")

def test_wrong_exit_5_3():
    # to test the output in case of no exit
    assert world.if_exit("5", "S") == ("No exit that way", "5")

def test_correct_exit_5_4():
    # to test in case of correct exit
    assert world.if_exit("5", "W") == ('You are standing in what seems to be a hall way connecting many room.', '2')

    
# Sixth Room
    
def test_correct_exit_6_1():
    # to test in case of correct exit
    assert world.if_exit("6", "S") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.', '9')

def test_correct_exit_6_2():
    # to test in case of correct exit
    assert world.if_exit("6", "N") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_6_3():
    # to test in case of correct exit
    assert world.if_exit("6", "E") == ('You are standing in a kitchen. Utensils everywhere.', '7')

def test_correct_exit_6_4():
    # to test in case of correct exit
    assert world.if_exit("6", "W") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.', '8')



# Seventh Room

def test_wrong_exit_7_1():
    # to test the output in case of no exit
    assert world.if_exit("7", "N") == ("No exit that way", "7")
    
def test_wrong_exit_7_2():
    # to test the output in case of no exit
    assert world.if_exit("7", "E") == ("No exit that way", "7")

def test_wrong_exit_7_3():
    # to test the output in case of no exit
    assert world.if_exit("7", "S") == ("No exit that way", "7")

def test_correct_exit_7_4():
    # to test in case of correct exit
    assert world.if_exit("7", "W") == ('You are standing in a connecting hallway. Three doors await you.', '6')


    
# Eigth Room

def test_wrong_exit_8_1():
    # to test the output in case of no exit
    assert world.if_exit("8", "N") == ("No exit that way", "8")

def test_wrong_exit_8_2():
    # to test the output in case of no exit
    assert world.if_exit("8", "W") == ("No exit that way", "8")

def test_correct_exit_8_3():
    # to test in case of correct exit
    assert world.if_exit("8", "S") == ('You are standing in the balcony of room number 8.', '10')

def test_correct_exit_8_4():
    # to test in case of correct exit
    assert world.if_exit("8", "E") == ('You are standing in a connecting hallway. Three doors await you.', '6')


# Ninth Room

def test_wrong_exit_9_1():
    # to test the output in case of no exit
    assert world.if_exit("9", "E") == ("No exit that way", "9")

def test_wrong_exit_9_2():
    # to test the output in case of no exit
    assert world.if_exit("9", "W") == ("No exit that way", "9")

def test_correct_exit_9_3():
    # to test in case of correct exit
    assert world.if_exit("9", "N") == ('You are standing in a connecting hallway. Three doors await you.', '6')

def test_correct_exit_9_4():
    # to test in case of correct exit
    assert world.if_exit("9", "S") == ('You are standing in the balcony of room number 9.', '11')

# Tenth Room

def test_wrong_exit_10_1():
    # to test the output in case of no exit
    assert world.if_exit("10", "W") == ("No exit that way", "10")
    
def test_wrong_exit_10_2():
    # to test the output in case of no exit
    assert world.if_exit("10", "E") == ("No exit that way", "10")

def test_wrong_exit_10_3():
    # to test the output in case of no exit
    assert world.if_exit("10", "S") == ("No exit that way", "10")

def test_correct_exit_10_4():
    # to test in case of correct exit
    assert world.if_exit("10", "N") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.', '8')

# Eleventh Room

def test_wrong_exit_11_1():
    # to test the output in case of no exit
    assert world.if_exit("11", "W") == ("No exit that way", "11")
    
def test_wrong_exit_11_2():
    # to test the output in case of no exit
    assert world.if_exit("11", "E") == ("No exit that way", "11")

def test_wrong_exit_11_3():
    # to test the output in case of no exit
    assert world.if_exit("11", "S") == ("No exit that way", "11")

def test_correct_exit_11_4():
    # to test in case of correct exit
    assert world.if_exit("11", "N") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.', '9')

def test_save_file():
    file_name = {"PLAYER": "3", "Vase": ["1", "There is a blue vase in the room."], "Knife": ["7", "You can see a knife in front of you."], "Ball": ["5", "There is a red tennis ball in front of you."], "0": ["You are standing at the end of a corridor. There is a door in front of you.", ["S", "1"]], "1": ["You are standing in what seems to be a living room.", ["E", "2"], ["N", "0"]], "2": ["You are standing in what seems to be a hall way connecting many room.", ["W", "1"], ["N", "3"], ["E", "5"], ["S", "6"]], "3": ["Your are standing in what seems to be a bedroom. It has got a balcony attached.", ["E", "4"], ["S", "2"]], "4": ["You are standing in the balcony of Room number 3.", ["W", "3"]], "5": ["You are standing in the balcony attached to the hallway.", ["W", "2"]], "6": ["You are standing in a connecting hallway. Three doors await you.", ["N", "2"], ["S", "9"], ["E", "7"], ["W", "8"]], "7": ["You are standing in a kitchen. Utensils everywhere.", ["W", "6"]], "8": ["You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.", ["E", "6"], ["S", "10"]], "9": ["You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.", ["N", "6"], ["S", "11"]], "10": ["You are standing in the balcony of room number 8.", ["N", "8"]], "11": ["You are standing in the balcony of room number 9.", ["N", "9"]]}

    world.save_file(file_name)

    wrapper = open("./maps.json", "r+")
    data = wrapper.readline()
    load = json.loads(data)
    assert load["PLAYER"] == "3"


def test_object_description():
    assert world.object_description('1') == 'There is a blue vase in the room.'
