# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        if self.current_room == "outside":
            return f"{self.name} is currently {self.current_room}"
        elif self.current_room == "treasure":
            return f"{self.name} is currently in the {self.current_room} room"
        else:
            return f"{self.name} is currently in the {self.current_room}"
