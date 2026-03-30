import unittest
from player import Player
from player_bst import PlayerBST
from player_bnode import PlayerBNode

class MyTests(unittest.TestCase):
    def test_custom(self):
        tree = PlayerBST()
        my_player1 = Player("1", "Alex")
        my_player2 = Player("2", "Brian")
        my_player3 = Player("3", "Charlie")
        my_player4 = Player("4", "Devon")
        my_player5 = Player("5", "Alex")
        my_player6 = Player("6", "Eric")
        tree.root = tree.insert(tree.root, my_player3)
        tree.root = tree.insert(tree.root, my_player1)
        tree.root = tree.insert(tree.root, my_player2)
        tree.root = tree.insert(tree.root, my_player4)
        tree.root = tree.insert(tree.root, my_player5)
        tree.root = tree.insert(tree.root, my_player6)
        self.assertEqual(tree.root.player, "Charlie")
        self.assertEqual(tree.root.left.player, "Alex")
        self.assertEqual(tree.root.left.right.player, "Brian")
        self.assertEqual(tree.root.right.player, "Devon")
        self.assertEqual(tree.root.right.right.player, "Eric")