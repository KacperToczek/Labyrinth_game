class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce_yourself(self):
        return "My name is {}. I have {} level. I'm dangerous!!!! \n".format(self.name, self.level)

