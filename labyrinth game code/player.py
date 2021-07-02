class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.items = []
        self.labyrinth = None
        self.current_chamber = None

    def get_info(self):
        return "{} \n level: {} \n value of items in backpack: {} $ \n" \
               " labyrinth: {} \n".format(self.name, self.level, self.value_of_items() ,self.labyrinth.name)

    def get_items(self):
        if self.items == []:
            return "Your backpack is empty. \n"
        output = "You have got following items: \n"
        i = 0
        for item in self.items:
            output += "{} - {}".format(i, item.get_description()) + "\n"
            i += 1
        return output

    def value_of_items(self):
        value = 0
        for item in self.items:
            value += item.value
        return value

    def look_around(self):
        return self.current_chamber.get_description()

    def check_doors(self):
        output = ""
        for door in self.current_chamber.doors:
            output += door.check_status()
            if door.needed_key in self.items and door.status != "open":
                output += "You can open this door. \n"
            elif door.needed_key in self.items and door.status == "open":
                output += "You opened this door earlier. \n"
            else:
                output += "You can't open this door. Find key! \n"
        return output

    def open_door(self, door):
        if door.needed_key in self.items and door.status == "closed":
            door.status = "open"
            return "You opened the door. \n"
        elif door.status == "open":
            return "{} has been opened \n".format(door.name)
        elif door.needed_key not in self.items:
            return "First find the key. \n"

    def change_chamber(self, door):
        self.current_chamber = door.connection[1]
        return "You changed chamber! \n"

    def take_item(self, item):
        self.items.append(item)
        self.current_chamber.items.remove(item)

    def drop_item(self, item):
        self.items.remove(item)
        self.current_chamber.items.append(item)