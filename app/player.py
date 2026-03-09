class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def __str__(self):
        return f"Player({self.uid}): '{self.name}'"

    @classmethod
    def hash(cls, key: str) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total

    def __hash__(self):
        return self.hash(self.uid)

    def __eq__(self, other):
        """
        Compares two players.
        useful for testing, and its customary that two players returning the same hash be considered equal
        """
        return self.uid == other.uid