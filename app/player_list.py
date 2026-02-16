from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    #Getters & Setters
    @property
    def head(self):
        return self._head
    @property
    def tail(self):
        return self._tail
    @head.setter
    def head(self, new_head):
        self._head = new_head
    @tail.setter
    def tail(self, new_tail):
        self._tail = new_tail

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, player):
        new_node = PlayerNode(player)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node