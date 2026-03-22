import unittest

from player import Player
from player_list import PlayerList
from player_hash_map import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):
    """
    Tests cover:
    - all methods in hash map
    - handle edge cases (adding, retrieving, and removing players from the hash map)
    """
    
    def test_init(self):
        map1 = PlayerHashMap()

        # correct map length
        self.assertEqual(10, len(map1.hashmap))
        # fill map with different PlayerList objects
        self.assertIsInstance(map1.hashmap[0], PlayerList)
        self.assertIsNot(map1.hashmap[0], map1.hashmap[1])

    def test_getitem(self):
        map1 = PlayerHashMap()
        self.assertEqual(ord("5") % 10, map1.__getitem__("5"))

    def test_setitem(self):
        map1 = PlayerHashMap()
        map1.__setitem__("1", "Alpha")
        self.assertEqual(map1.hashmap[9].head.key, "1")
        self.assertEqual(map1.hashmap[9].head.name, "Alpha")
        map1.__setitem__("1", "Alex")
        self.assertEqual(map1.hashmap[9].head.name, "Alex")

    def test_delitem(self):
        map1 = PlayerHashMap()
        map1.__setitem__("1", "Alpha")
        self.assertEqual(map1.hashmap[9].head.key, "1")
        self.assertEqual(map1.hashmap[9].head.name, "Alpha")
        map1.__delitem__("1")
        self.assertIsNone(map1.hashmap[9].head)

    def test_len(self):
        map1 = PlayerHashMap()
        map1.__setitem__("1", "Alpha")
        map1.__setitem__("2", "Bravo")
        map1.__setitem__("3", "Charlie")
        self.assertEqual(3, len(map1))

    def test_display(self):
        map1 = PlayerHashMap()
        map1.__setitem__("1", "Alpha")
        map1.__setitem__("2", "Bravo")
        map1.__setitem__("3", "Charlie")
        map1.__setitem__("4", "Delta")
        map1.__setitem__("5", "Echo")
        map1.__setitem__("6", "Foxtrot")
        map1.__setitem__("7", "Golf")
        map1.__setitem__("8", "Hotel")
        map1.__setitem__("9", "India")
        map1.__setitem__("10", "Juliet")
        map1.__setitem__("11", "Kilo")
        map1.__setitem__("12", "Lima")
        map1.__setitem__("13", "Mike")
        map1.__setitem__("14", "November")
        map1.__setitem__("15", "Oscar")
        map1.__setitem__("16", "Papa")
        map1.__setitem__("17", "Quebec")
        map1.__setitem__("18", "Romeo")
        map1.__setitem__("19", "Sierra")
        map1.__setitem__("20", "Tango")
        map1.__setitem__("21", "Uniform")
        map1.__setitem__("22", "Victor")
        map1.__setitem__("23", "Whiskey")
        map1.__setitem__("24", "Xray")
        map1.__setitem__("25", "Yankee")
        map1.__setitem__("26", "Zulu")
        map1.display()