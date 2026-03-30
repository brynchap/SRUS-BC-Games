from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self.root = None

    @property
    def root_property(self):
        return self.root

    def insert(self, root, player: Player):
        key = player.name
        # If the tree is empty, return a new node
        if root is None:
            return PlayerBNode(key)
        # Otherwise, recur down the tree
        if key == root.player: # Handle Duplicates by overwriting them but keeping the old left and right values
            node = PlayerBNode(key)
            node.left = root.left
            node.right = root.right
            return node
        if key < root.player: #left
            root.left = self.insert(root.left, player)
        else: # right
            root.right = self.insert(root.right, player)
        # Return the (unchanged) node pointer
        return root