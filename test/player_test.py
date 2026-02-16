import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_properties(self):
        my_player = Player("1", "John")
        self.assertIs(my_player.uid, "1")
        self.assertIs(my_player.name, "John")

