from item import Item


class Key(Item):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.which_door = []

    def get_which_door(self):
        return self.which_door

    def get_description(self):
        output = "{}, it is worth {} $, it opens: ".format(self.name, self.value)
        for door in self.which_door:
            output += door.name + ", "
        return output
