class PlayerBNode:
    def __init__(self, player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, new_left):
        self._left = new_left

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, new_right):
        self._right = new_right