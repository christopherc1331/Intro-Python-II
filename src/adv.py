from room import Room
from player import Player

# Declare all the rooms

rooms = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
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


key_list = list(rooms.keys())
val_list = list(rooms.values())


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Jakob", rooms["outside"])

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
allowed_entries = ("n", "e", "s", "w", "q")
entry = ""


while entry != "q":
    print("")
    print("=========================")
    print(player1)
    print("=========================")
    print("")
    entry = input("Enter a direction. Enter q to quit: ")

    while entry not in allowed_entries:
        print("")
        print("=========================")
        entry = input("Invalid entry. Enter either: n,e,s,w, or q (to quit)")

    if entry != "q":
        try:
            current_room_key = key_list[val_list.index(player1.current_room)]
            destinationObj = getattr(rooms[current_room_key], f"{entry}_to")
            destination_room_key = key_list[val_list.index(destinationObj)]
            player1.current_room = destinationObj
            print("=========================")
            print("")
            print(f"{player1.name} went {entry} to {destinationObj.name}")
            print("=========================")
            print("")
        except:
            print("")
            print("=========================")
            print("You can't go that way")
