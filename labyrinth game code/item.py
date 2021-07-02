class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_description(self):
        return "{}, it is worth {} $".format(self.name, self.value)
