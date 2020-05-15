# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description, item_list=[]):
        self.name = name
        self.description = description
        self.item_list = item_list

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_item_to_room(self, item):
        self.item_list.append(item)

    def remove_item_from_room(self, item):
        self.item_list.remove(item)

    def print_items_in_room(self):
        print(f"------------Visible Items------------")
        print("______________________________________")
        print("")
        for index, item in enumerate(self.item_list):
            print(f"{index + 1}: {item.name} - {item.description}")
