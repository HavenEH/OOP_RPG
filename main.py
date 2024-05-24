class Map:

    def __init__(self, tile_name, tile_description):
        self.tile_name = tile_name
        self.tile_description = tile_description

    def print_tile_name(self):
        print(str("you are in ") + (self.tile_name))

    def print_tile_description(self):
        print(self.tile_description)


A1 = Map("room A1", "This is room A1")
A2 = Map("room A2", "This is room A2")
A3 = Map("room A3", "This is room A3")
B1 = Map("room B1", "This is room B1")
B2 = Map("room B2", "This is room B2")
B3 = Map("room B3", "This is room B3")
C1 = Map("room C1", "This is room C1")
C2 = Map("room C2", "This is room C2")
C3 = Map("room C3", "This is room C3")

map_array = [[A1, A2, A3], [B1, B2, B3], [C1, C2, C3]]

inv = []


class Player:

    def __init__(self, x, y, action):
        self.location = [x, y]
        self.action = action
        self.swordget = False

    def act_choice(self):
        action_choose = input(
            "What would you like to do? m = move, i = inventory")
        if action_choose == "m":
            self.move_player
        elif action_choose == "i":
            print (inv)
        else:
            print("Please choose a valid action")
            self.act_choice()

    def item_get(self):
        if self.location == [1, 1] and not self.swordget:
            pickupC = input(
                "would you like to pick up the sword (type y or n)")
            if pickupC == "y":
                self.swordget = True
                print("you have picked up the sword")
                inv.append("sword")
            elif pickupC == "n":
                evan.move_player()

        
        else:
            pass

    def move_player(self):
        move = input("which way do you want to go?(type m to open menu)\n")
        if move == "w":
            self.location[1] -= 1
        elif move == "s":
            self.location[1] += 1
        elif move == "a":
            self.location[0] -= 1
        elif move == "d":
            self.location[0] += 1
        elif move == "m":
            evan.act_choice()    
        else:
            print("invalid input")
            self.move_player()
            

        if self.location[0] > 2:
            self.location[0] = 2
            print("you can't go that way")
        elif self.location[0] < 0:
            self.location[0] = 0
            print("you can't go that way")
        elif self.location[1] > 2:
            self.location[1] = 2
            print("you can't go that way")
        elif self.location[1] < 0:
            self.location[1] = 0
            print("you can't go that way")
            
        
        map_array[self.location[1]][self.location[0]].print_tile_name()
        map_array[self.location[1]][self.location[0]].print_tile_description()
        input()

        self.item_get()

        evan.move_player()


evan = Player(0, 0, "action")
evan.move_player()

#map_array[y][x].move_player()
"""def __init__(self, x, y):
        self.x = x
        self.y = y

    def Location(self):
        if self.x == 0 and self.y == 0:
            return "B2"
        elif self.x == 0 and self.y == 1:
            return "A2"
        elif self.x == 1 and self.y == 0:
            return "B3"
        elif self.x == -1 and self.y == 0:
            return "B1"
        elif self.x == 0 and self.y == -1:
            return "C2"
        elif self.x == 1 and self.y == 1:
            return "A3"
        elif self.x == -1 and self.y == -1:
            return "C1"
        elif self.x == 1 and self.y == -1:
            return "C3"
        elif self.x == -1 and self.y == 1:
            return "A1"
        else:
            return "I have no clue where you are."


class Map:
    def location(x, y):
        if x == 0 and y == 0:
            return "B2"
        elif x == 0 and y == 1:
            return "A2"
        elif x == 1 and y == 0:
            return "B3"
        elif x == -1 and y == 0:
            return "B1"
        elif x == 0 and y == -1:
            return "C2"
        elif x == 1 and y == 1:
            return "A3"
        elif x == -1 and y == -1:
            return "C1"
        elif x == 1 and y == -1:
            return "C3"
        elif x == -1 and y == 1:
            return "A1"
        else:
            return "I have no clue where you are." 







def loc_info(playr_x, playr_y):
    if (Map.Location(playr_x, playr_y)) == "A1":
        print("\nYou are in room A1")
    elif (Map.Location(playr_x, playr_y)) == "A2":
        print("\nyou are in room A2")
    elif (Map.Location(playr_x, playr_y)) == "A3":
        print("\nyou are in room A3")
    elif (Map.Location(playr_x, playr_y)) == "B1":
        print("\nyou are in room B1")
    elif (Map.Location(playr_x, playr_y)) == "B2":
        print("\nyou are in room B2")
    elif (Map.Location(playr_x, playr_y)) == "B3":
        print("\nyou are in room B3")
    elif (Map.Location(playr_x, playr_y)) == "C1":
        print("\nyou are in room C1")
    elif (Map.Location(playr_x, playr_y)) == "C2":
        print("\nyou are in room C2")
    elif (Map.Location(playr_x, playr_y)) == "C3":
        print("\nyou are in room C3")




loc = Map(0, 0)

loc.x = 1 
loc.y = 1

print(loc.Location())

def loc_info():
    if loc.x == -1 and loc.y == 1:
        print("You are in room A1")
    elif loc.x == 0 and loc.y == 1:
        print("you are in room A2")
    elif loc.x == 1 and loc.y == 1:
        print("you are in room A3")
    elif loc.x == -1 and loc.y == 0:
        print("you are in room B1")
    elif loc.x == 0 and loc.y == 0:
        print("you are in room B2")
    elif loc.x == 1 and loc.y == 0:
        print("you are in room B3")
    elif loc.x == -1 and loc.y == -1:
        print("you are in room C1")
    elif loc.x == 0 and loc.y == -1:
        print("you are in room C2")
    elif loc.x == 1 and loc.y == -1:
       print("you are in room C3")
    



loc_info()"""
