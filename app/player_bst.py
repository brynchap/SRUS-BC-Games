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
            return PlayerBNode(player)
        # Otherwise, recur down the tree
        if key == root.player.name: # Handle Duplicates by overwriting them but keeping the old left and right values
            node = PlayerBNode(player)
            node.left = root.left
            node.right = root.right
            return node
        if key < root.player.name: #left
            root.left = self.insert(root.left, player)
        else: # right
            root.right = self.insert(root.right, player)
        # Return the (unchanged) node pointer
        return root

    def search(self, root, name):
        key = name
        if root is None:
            return None
        if key == root.player.name: # Handle Duplicates by overwriting them but keeping the old left and right values
            return root
        if key < root.player.name: #left
            return self.search(root.left, name)
        else: # right
            return self.search(root.right, name)