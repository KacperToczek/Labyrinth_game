import unittest
from labyrinth import Labyrinth
from player import Player
from key import Key
from door import Door


class Test(unittest.TestCase):
    def setUp(self):
        self.lab = Labyrinth("labyrinth", "Kacper")
        self.player2 = Player("Player2")

    def test_add_player(self):
        self.lab.add_player(self.player2)
        self.assertEqual(self.lab.player.name, "Kacper")

    def test_add_chamber(self):
        self.lab.add_chambers([self.player2])
        self.assertFalse(self.player2 in self.lab.chambers)

    def test_needed_key(self):
        for chamber in self.lab.chambers:
            for door in chamber.doors:
                self.assertNotEqual(door.needed_key, None)

    def test_which_door(self):
        for chamber in self.lab.chambers:
            for item in chamber.items:
                if isinstance(item, Key):
                    for door in item.which_door:
                        self.assertTrue(isinstance(door, Door))

    def test_take_item(self):
        item = self.lab.chambers[0].items[0]
        self.lab.player.take_item(item)
        self.assertFalse(item in self.lab.chambers[0].items)

    def test_drop_item(self):
        item = self.lab.chambers[0].items[0]
        self.lab.player.take_item(item)
        self.lab.player.drop_item(item)
        self.assertEqual(self.lab.player.items, [])

    def test_monster_duel(self):
        for chamber in self.lab.chambers:
            if chamber.monster != None:
                self.assertTrue(chamber.duel != None)


if __name__ == '__main__':
    unittest.main()
