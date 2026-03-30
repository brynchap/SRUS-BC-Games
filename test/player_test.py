import unittest
from player import Player
import random

class TestPlayer(unittest.TestCase):
    def test_properties(self):
        my_player = Player("1", "John")
        self.assertEqual(my_player.uid, "1")
        self.assertEqual(my_player.name, "John")

    def test_sort_players(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5),
                   Player(name="Charlie", uid='03', score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(name="Bob", uid='02', score=5), Player(name="Alice", uid='01', score=10),
                                   Player(name="Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(name="Alice", uid='01', score=10)
        bob = Player(name="Bob", uid='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob)
        # or, event better
        self.assertGreater(alice, bob)

    def test_sort_quickly(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5),
                   Player(name="Charlie", uid='03', score=15)]
        quickly_sorted_players = Player.sort_quickly(players)
        manually_sorted_players = [Player(name="Charlie", uid='03', score=15), Player(name="Alice", uid='01', score=10),
                                   Player(name="Bob", uid='02', score=5)]
        self.assertListEqual(quickly_sorted_players, manually_sorted_players)

    def test_sort_1000_quickly(self):
        players = [Player(name=f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
        quickly_sorted_players = Player.sort_quickly(players)
        sorted_players = sorted(players, reverse=True)
        scores_quickly_sorted_players = []
        scores_sorted_players = []
        for player in quickly_sorted_players:
            scores_quickly_sorted_players.append(player.score)
        for player in sorted_players:
            scores_sorted_players.append(player.score)
        self.assertListEqual(scores_quickly_sorted_players, scores_sorted_players)

    def test_sort_1000_presorted_players(self):
        players = [Player(name=f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
        pre_sorted_players = sorted(players, reverse=True)
        new_sorted_players = Player.sort_quickly(pre_sorted_players)
        scores_pre_sorted_players = []
        scores_new_sorted_players = []
        for player in pre_sorted_players:
            scores_pre_sorted_players.append(player.score)
        for player in new_sorted_players:
            scores_new_sorted_players.append(player.score)
        self.assertListEqual(scores_pre_sorted_players, scores_new_sorted_players)