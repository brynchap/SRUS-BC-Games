class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._previous = None

    #Getters
    @property
    def key(self):
        return self._player.uid
    @property
    def next(self):
        return self._next
    @property
    def previous(self):
        return self._previous
    #Setters
    def set_next(self, new_next):
        self._next = new_next
    def set_previous(self, new_previous):
        self._previous = new_previous

    def __str__(self):
        return f"Node: {self.key}, next: {self.next}, previous: {self.previous}"