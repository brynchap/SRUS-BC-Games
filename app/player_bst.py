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

    def balance(self, root):
        # turn BST into a list
        def convert_bst_to_sorted_array(node, result=None):
            if result is None:
                result = []
            if node:
                # 1. Traverse left subtree
                convert_bst_to_sorted_array(node.left, result)
                # 2. Visit root
                result.append(node.player)
                # 3. Traverse right subtree
                convert_bst_to_sorted_array(node.right, result)
            return result
        sorted_array = convert_bst_to_sorted_array(root)
        def convert_sorted_array_to_bbst(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = PlayerBNode(arr[mid])

            #build left and right subtrees
            root.left = convert_sorted_array_to_bbst(arr[:mid])
            root.right = convert_sorted_array_to_bbst(arr[mid+1:])
            return root
        return convert_sorted_array_to_bbst(sorted_array)