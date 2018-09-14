import world

maps = world.load_file()
player_pos = maps["PLAYER"]
print(maps[player_pos][0])
while True:
    direction = input("Enter Direction: ")
    description, player_pos, object_in_room  = world.if_exit(player_pos, direction)
    print(description)
    print(object_in_room)
    print(world.get_exits(player_pos))
    world.save_file(maps)
    
    
