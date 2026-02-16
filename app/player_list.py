from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, player):
        new_node = PlayerNode(player)
        new_node.set_next(self.head)
        if self.head:
            self.head.set_previous(new_node)
        self.head = new_node