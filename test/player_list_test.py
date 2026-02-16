import unittest
from player import Player
from player_node import PlayerNode
from player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_add(self):
        my_player = Player("1", "John")
        my_player2 = Player("2", "Bob")
        my_list = PlayerList()

        self.assertEqual(my_list.head, None)
        my_list.insert_at_head(my_player)
        self.assertEqual(my_list.head.key, "1")
        my_list.insert_at_head(my_player2)
        self.assertEqual(my_list.head.key, "2")
        self.assertEqual(my_list.head.next.key, "1")
        self.assertEqual(my_list.head.next.previous.key, "2")