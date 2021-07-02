class Door:
    def __init__(self, name, from_chamber, to_chamber):
        self.name = name
        self.connection = [from_chamber, to_chamber]
        self.status = "closed"
        self.needed_key = None

    def get_needed_key(self):
        return "To open the {} you need a {}.".format(self.name, self.needed_key.name)

    def check_status(self):
        return "The {} is {}. ".format(self.name, self.status)

    def change_status(self):
        self.status = "open"
