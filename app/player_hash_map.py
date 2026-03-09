from player_list import PlayerList
from player import Player

class PlayerHashMap(): #handle collisions by chaining player data using PlayerList data structure
    """
    Methods:
    --------

    put(key, name) OR __setitem__(key, name)
    Add a new player to PlayerList in corresponding index in hash map.

    get(key) OR __getitem__(key)
    Retrieve player from PlayerList with corresponding index in hash map.

    remove(key) OR __delitem__(key)
    Remove player from PlayerList with corresponding index in hash map

    size() OR __len__()
    Return number of players in hash map
    """

    SIZE: int = 10
    def __init__(self):
        self.hashmap = {}
        for i in range(self.SIZE):
            self.hashmap[i] = PlayerList()

    def __getitem__(self, key: str | Player) -> int:
        if isinstance(key, Player): # if key is part of a player class
            return hash(key) % self.SIZE # using basic Unicode
        else:
            return Player.hash(key) % self.SIZE # using sum of Unicode

    def __setitem__(self, key: str, name: str) -> None:
        """ Psuedo code:
        1. Use the key to calculate an index into the hash map
            (TODO: Implement a hash function in the Player class that returns a player hash and then modulate it by the size of the hashmap)
        2. Get the PlayerList at that index
        3. Check if the player is already on that player list.
            If it is, update the player's name.
            If it isn't, create a player and add the player to the player list.
             """
        player_list = self.hashmap[self.__getitem__(key)]

        current = player_list.head
        is_in_list = False
        while current is not None: #Check if the player is already on that player list.
            if current.uid == key: #If it is, update the player's name.
                current.name = name
                is_in_list = True
                break
            current = current.next
        if not is_in_list:
            new_player = Player(uid = key, name = name)
            player_list.insert_at_head(new_player)

    def __delitem__(self, key):
        player_list = self.hashmap[self.__getitem__(key)]
        player_list.delete_key(key)

    def __len__(self):
        """Return number of players in the hash map"""
        number_of_players = 0
        for i in self.hashmap:
            current = self.hashmap[i].head
            while current is not None:
                number_of_players += 1
                current = current.next
        return number_of_players

