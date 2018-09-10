import world

maps = world.load_file()
player_pos = maps["PLAYER"]
print(maps[player_pos][0])
while True:
    direction = input("Enter Direction: ")
    description, player_pos = world.if_exit(player_pos, direction)
    print(description)
    world.save_file(maps)
    