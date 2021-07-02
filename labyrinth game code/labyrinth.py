from chamber import Chamber
from door import Door
from item import Item
from key import Key
from monster import Monster
from player import Player
from task import Task


class Labyrinth:
    def __init__(self, name, player_name):
        self.name = name
        self.player = None
        self.player_name = player_name
        self.chambers = []
        self.tasks = []
        self.map = None
        return self.create_labyrinth()

    def get_description(self):
        description = "Hello {},\n" \
                      "You are in labyrinth '{}' \n" \
                      "Get as many valuable items as possible. Do it as soon as possible. \n" \
                      "In this labyrinth there are {} chambers: \n".format(self.player.name,self.name, len(self.chambers))
        for chamber in self.chambers:
            description += "-" + chamber.name + "\n"
        description += "Currently, you are in {} , " \
                       "find the exit from labyrinth!!!!! \n".format(self.player.current_chamber.name)
        return description

    def add_player(self, player):
        if isinstance(player, Player) and self.player == None:
            self.player = player
            self.player.labyrinth = self

    def add_chambers(self, chambers):
        for chamber in chambers:
            if isinstance(chamber, Chamber):
                self.chambers.append(chamber)
                chamber.labyrinth = self
                if chamber.start:
                    self.player.current_chamber = chamber

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)

    def create_labyrinth(self):
        player = Player(self.player_name)
        self.add_player(player)

        ch1 = Chamber("Silver chamber", start=True)
        ch2 = Chamber("Gold chamber")
        ch3 = Chamber("Scarlet chamber")
        ch4 = Chamber("Sapphire chamber")
        ch5 = Chamber("Platinum chamber", final=True)

        self.add_chambers([ch1, ch2, ch3, ch4, ch5])

        key1 = Key("key (Silver-Gold)", 100)
        key2 = Key("key (Gold-Scarlet)", 100)
        key3 = Key("key (Sapphire-Sapphire)", 100)
        key4 = Key("key (Gold-Platinum)", 100)

        ch1.add_door(Door("door1 (Silver)", ch1, ch2), key1)
        ch2.add_door(Door("door1 (Gold)", ch2, ch1), key1)
        ch2.add_door(Door("door2 (Gold)", ch2, ch3), key2)
        ch2.add_door(Door("door3 (Gold)", ch2, ch5), key4)
        ch3.add_door(Door("door1 (Scarlet)", ch3, ch2), key2)
        ch3.add_door(Door("door2 (Scarlet)", ch3, ch4), key3)
        ch4.add_door(Door("door1 (Sapphire)", ch4, ch3), key3)

        self.add_task(Task("2 + 2 = 4 , True or False?", "True"))
        self.add_task(Task("2 * 3 = 7 , True or False?", "False"))
        self.add_task(Task("5! = 120 , True or False?", "True"))
        self.add_task(Task("2 + 2 * 2 = 6, True or False?", "True"))
        self.add_task(Task("2 + 2 * 2 = 8, True or False?", "False"))

        ch1.add_item(Item("gold bar", 10000))
        ch2.add_item(Item("silver bar", 5000))
        ch3.add_item(Item("gold coin", 100))
        ch4.add_item(Item("silver coin", 50))
        ch3.add_item(Item("copper coin", 10))
        ch4.add_item(Item("box of gold coins", 2400))
        ch2.add_item(Item("box of silver coins", 1200))
        ch2.add_item(Item("pouch with gold coins", 800))
        ch4.add_item(Item("pouch with silver coins", 400))
        ch3.add_item(Item("pouch with copper coins", 80))
        ch2.add_item(Item("diamond", 600))
        ch3.add_item(Item("pouch with diamonds", 3000))
        ch1.add_item(Item("box of diamonds", 9000))

        ch1.add_item(key1)
        ch2.add_item(key2)
        ch3.add_item(key3)
        ch4.add_item(key4)

        ch2.add_monster(Monster("Ghost", 10))
        ch3.add_monster(Monster("Vampire", 7))
        ch4.add_monster(Monster("Werewolf", 6))

        self.map = " __________________________________\n" \
              "|Silver     |Sapphire              |\n" \
              "|           |                      |\n" \
              "|           |                      |\n" \
              "|_______D___|__________            |\n" \
              "|Gold       |Scarlet   |           |\n" \
              "|           |          D           |\n" \
              "|           |____D_____|___________|\n" \
              "|                      |   Platinum|\n" \
              "|                      D           |\n" \
              "|______________________|___________|"