class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Store the node's value and point 'next' at nothing yet -
        it gets wired up later when the node is linked into a list.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """An empty list simply has no head yet."""
        self.head = None

    def insert_at_front(self, data):
        """
        O(1): the new node just points at the old head, then
        becomes the head itself. No traversal needed.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        O(n): have to walk the whole list to find the last node,
        since we don't keep a separate 'tail' pointer.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Base case: an empty node contributes 0.
        Recursive case: this node's data plus the sum of everything after it.
        """
        def _sum(node):
            if node is None:
                return 0
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        """
        Base case: we've walked off the end (current is None) -
        'prev' is now the last node we visited, i.e. the new head.
        Recursive case: flip current's 'next' to point backward at
        'prev', then move one step forward and recurse.
        """
        def _reverse(prev, current):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev
            return _reverse(current, next_node)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """
        Base cases: ran off the end (not found) or found a match.
        Recursive case: keep looking down the rest of the list.
        """
        def _search(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search(node.next)

        return _search(self.head)

    def display(self):
        """Print the list as 'val -> val -> ... -> None'."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        print(" -> ".join(values))