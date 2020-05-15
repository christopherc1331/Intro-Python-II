# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        if self.current_room == "outside":
            return f"{self.name} is currently {self.current_room}"
        elif self.current_room == "treasure":
            return f"{self.name} is currently in the {self.current_room} room"
        else:
            return f"{self.name} is currently in the {self.current_room}"

    def print_items_in_inventory(self):
        print(f"---------Items In Inventory---------")
        print("______________________________________")

        for index, item in enumerate(self.inventory):
            print(f"{index + 1}: {item.name} - {item.description}")

    def add_item_to_inventory(self, new_item):
        self.inventory.append(new_item)

    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)
