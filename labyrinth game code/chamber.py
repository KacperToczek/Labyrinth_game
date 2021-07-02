from duel import Duel
from door import Door
from key import Key
from item import Item
from monster import Monster


class Chamber:
    def __init__(self, name, start=False, final=False):
        self.name = name
        self.start = start
        self.final = final
        self.labyrinth = None
        self.doors = []
        self.items = []
        self.monster = None
        self.duel = None

    def add_door(self, door, key):
        if isinstance(door, Door) and isinstance(key, Key):
            door.needed_key = key
            key.which_door.append(door)
            self.doors.append(door)

    def add_item(self, item):
        if isinstance(item, Item):
            self.items.append(item)

    def add_monster(self, monster):
        if isinstance(monster, Monster) and self.monster == None:
            self.monster = monster
            self.duel = Duel(self.labyrinth.player, self.monster)

    def get_description(self):
        output = "You are in {} . \n".format(self.name)
        if self.items != []:
            output += "There are items such as: \n"
            for item in self.items:
                output += "-" + item.get_description() + "\n"
        if self.doors != []:
            output += "From here you can go to: \n"
            for door in self.doors:
                output += "-" + "through {} to {} \n".format(door.name, door.connection[1].name)
        if self.monster is not None:
            output += "Here you will meet monster: {}. \n".format(self.monster.name)
        return output

    def get_items(self):
        output = ""
        i = 0
        for item in self.items:
            output += "{} - {}".format(i, item.name) + "\n"
            i += 1
        return output

    def get_doors(self):
        output = ""
        i = 0
        for door in self.doors:
            output += "{} - {}, {} behind this door".format(i, door.name, door.connection[1].name) + "\n"
            i += 1
        return output
