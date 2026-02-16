import unittest
from player import Player
from player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_add_from_head(self):
        my_player = Player("1", "John")
        my_player2 = Player("2", "Bob")
        my_list = PlayerList()

        self.assertEqual(my_list.head, None)
        self.assertEqual(my_list.tail, None)
        my_list.insert_at_head(my_player)
        self.assertEqual(my_list.head.key, "1")
        my_list.insert_at_head(my_player2)
        self.assertEqual(my_list.head.key, "2")
        self.assertEqual(my_list.head.next.key, "1")
        self.assertEqual(my_list.head.next.previous.key, "2")
        self.assertEqual(my_list.tail.key, "1")

    def test_add_from_tail(self):
        my_player = Player("1", "John")
        my_player2 = Player("2", "Bob")
        my_list = PlayerList()

        self.assertEqual(my_list.head, None)
        self.assertEqual(my_list.tail, None)
        my_list.insert_at_tail(my_player)
        self.assertEqual(my_list.head.key, "1")
        self.assertEqual(my_list.tail.key, "1")
        my_list.insert_at_tail(my_player2)
        self.assertEqual(my_list.tail.key, "2")

    def test_delete_head(self):
        my_player = Player("1", "Alex")
        my_player2 = Player("2", "Bob")
        my_player3 = Player("3", "Charlie")
        my_list = PlayerList()

        my_list.insert_at_head(my_player)
        my_list.insert_at_head(my_player2)
        my_list.insert_at_head(my_player3)
        self.assertEqual(my_list.head.key, "3")
        my_list.delete_head()
        self.assertEqual(my_list.head.key, "2")
        self.assertEqual(my_list.head.previous, None)

    def test_delete_tail(self):
        my_player = Player("1", "Alex")
        my_player2 = Player("2", "Bob")
        my_player3 = Player("3", "Charlie")
        my_list = PlayerList()

        my_list.insert_at_head(my_player)
        my_list.insert_at_head(my_player2)
        my_list.insert_at_head(my_player3)
        self.assertEqual(my_list.tail.key, "1")
        my_list.delete_tail()
        self.assertEqual(my_list.tail.key, "2")
        self.assertEqual(my_list.tail.next, None)

    def test_delete_key(self):
        my_player = Player("1", "Alex")
        my_player2 = Player("2", "Bob")
        my_player3 = Player("3", "Charlie")
        my_list = PlayerList()

        my_list.insert_at_head(my_player)
        my_list.insert_at_head(my_player2)
        my_list.insert_at_head(my_player3)
        self.assertEqual(my_list.head.key, "3")
        my_list.delete_key("2")
        self.assertEqual(my_list.head.next.key, "1")