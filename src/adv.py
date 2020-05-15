from room import Room
from player import Player
from item import Item

# Declare all the rooms

rooms = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [
            Item("dirt", "Some dirt on the ground"),
            Item("jar", "Can be used to hold things"),
        ],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [Item("glass", "Thirsty?"), Item("light_bulb", "A viable light source"),],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [
            Item("frog", "Rrrribbbit!"),
            Item("coffee", "It's still warm..."),
            Item("pepper_spray", "The ultimate stay away juice"),
        ],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [Item("torch", "Should probably hang on to this")],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [
            Item("coin", "The only treasure left in this room"),
            Item("notepad", "I think I can see some writing on here"),
        ],
    ),
}


# Link rooms together

rooms["outside"].n_to = rooms["foyer"]
rooms["foyer"].s_to = rooms["outside"]
rooms["foyer"].n_to = rooms["overlook"]
rooms["foyer"].e_to = rooms["narrow"]
rooms["overlook"].s_to = rooms["foyer"]
rooms["narrow"].w_to = rooms["foyer"]
rooms["narrow"].n_to = rooms["treasure"]
rooms["treasure"].s_to = rooms["narrow"]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Jakob", rooms["outside"], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


#  "Markup" variables
space = ""
line = "========================="

directions = ("n", "e", "s", "w", "q")
direction = ""


def isDirection():
    if len(direction.split()) == 1:
        return True
    else:
        return False


while direction != "q":
    print(space)
    print(line)
    print(player1)
    print("")
    player1.current_room.print_items_in_room()
    print(space)
    print(line)
    player1.print_items_in_inventory()
    print(space)
    print(line)
    direction = input("Enter a direction. Enter q to quit: ")
    if isDirection():
        while direction not in directions:
            print(space)
            print(line)
            direction = input(
                "Invalid direction. Enter either: n,e,s,w, or q (to quit)"
            )

        if direction != "q":
            try:
                player1.current_room = getattr(player1.current_room, f"{direction}_to")
                print(space)
                print(line)
                print(f"{player1.name} went {direction} to {player1.current_room.name}")
                print(space)
                print(line)
            except:
                print(space)
                print(line)
                print(f"You can't go {direction} from here")
    else:
        verb, thing = direction.split()
        if verb == "take" or verb == "get":

            if thing in [item.name for item in player1.current_room.item_list]:
                for item in player1.current_room.item_list:
                    if item.name == thing:
                        player1.add_item_to_inventory(item)
                        player1.current_room.remove_item_from_room(item)
                        print(f"Picked up: {item.name}")
                        break
            else:
                print(space)
                print(line)
                print(f"{item.name} wasn't found in this room")
        elif verb == "drop":
            if thing in [item.name for item in player1.inventory]:
                for item in player1.inventory:
                    if item.name == thing:
                        player1.remove_item_from_inventory(item)
                        player1.current_room.add_item_to_room(item)
                        print(space)
                        print(line)
                        print(f"Dropped: {item.name}")
                        break
            else:
                print(space)
                print(line)
                print(f"{item.name} wasn't found in inventory")
        else:
            print("invalid entry")
