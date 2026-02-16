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

    def insert_at_tail(self, player):
        new_node = PlayerNode(player)
        new_node.previous = self.tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def delete_from_head(self, my_id):
        current = self.head
        previous = self.head

        while current.key != my_id:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.head:
            self.head = self.head.next
        else:
            previous.next = current.next
            if current.next:
                current.next.previous = current.previous
        return current

    def delete_from_tail(self, my_id):
        current = self.tail
        next = self.tail

        while current.key != my_id:
            if current.previous is None:
                return None
            else:
                next = current
                current = current.previous

        if current == self.tail:
            self.tail = self.tail.previous
        else:
            next.previous = current.previous
            if current.previous:
                current.previous.next = current.next

        return current