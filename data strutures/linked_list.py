# Demo Linked List
class Node: # Each node include two fields: data and next
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None): # Initialize a linked list
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self): # Visualize operations of linked list
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ' -> '.join(nodes)

    def __iter__(self): # Help object iterable
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, new_node): # Inserting node at the beginning of linked list
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node): # Inserting node at the ending of linked list
        if self.head is None:
            self.head = new_node
            return

        for current_node in self:
            pass
        current_node.next = new_node

    def add_after(self, target_node, new_node): # Inserting node at the after of specified node
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node)

    def add_before(self, target_node, new_node): # Inserting node at the before of specified node
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node)

    def remove_node(self, target_node): # Remove specific node
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node)

    def get_an_element(self, index): # Get an element with specific index
        if self.head is None:
            raise Exception("List is empty")

        count = 0 # Keep track until reach the element
        for node in self:
            if count == index:
                return node.data
            count += 1
        raise Exception("Index is out of range of list")

    def reverse(self): # Reverse the elements of linked list
        if self.head is None:
            raise Exception("List is empty")

        track_nodes = [] # Keep track nodes from the beginning to the end of the list
        while self.head is not None:
            track_nodes.append(self.head)
            self.head = self.head.next

        track_nodes.reverse()
        for buffer in track_nodes: # Set Next field of nodes to None
            buffer.next = None

        self.head = track_nodes.pop(0)
        node = self.head

        for element in track_nodes:
            node.next = element
            node = element

# Print out Linked list
llist = LinkedList(['a', 'b', 'c', 'd'])
print(llist) # return a -> b -> c -> d -> None

# Iterate and print each element in the Linked list
for node in llist:
    print(node)

# Insert at the beginning
llist2 = LinkedList()
llist2.add_first(Node("b"))
print(llist2) # return b -> None

llist2.add_first(Node("a"))
print(llist2) # return a -> b -> None

# Insert at the end
llist2.add_last(Node("e"))
print(llist2) # return a -> b -> e -> None

llist2.add_last(Node("f"))
print(llist2) # return a -> b -> e -> f -> None

# Insert after an existing node
llist3 = LinkedList()
llist3.add_after("a", Node("b")) # return Exception: List is empty

llist3 = LinkedList(["a", "b", "c", "d"])
llist3.add_after("c", Node("cc"))
print(llist3) # return a -> b -> c -> cc -> d -> None

llist3.add_after("f", Node("g")) # return Exception: Node with data 'f' not found

# Insert before an existing node
llist4 = LinkedList()
llist4.add_before("a", Node("a")) # return Exception: List is empty

llist4 = LinkedList(["b", "c"])
llist4.add_before("b", Node("a"))
print(llist4) # return a -> b -> c -> None

llist4.add_before("b", Node("aa"))
llist4.add_before("c", Node("bb"))
print(llist4) # return a -> aa -> b -> bb -> c -> None

llist4.add_before("n", Node("m")) # return Exception: Node with data 'n' not found

# Remove a node
llist5 = LinkedList()
llist5.remove_node("a") # return Exception: List is empty

llist5 = LinkedList(["a", "b", "c", "d", "e"])
print(llist5) # return a -> b -> c -> d -> e -> None

llist5.remove_node("a")
print(llist5) # return b -> c -> d -> e -> None

llist5.remove_node("e")
print(llist) # return b -> c -> d -> None

llist5.remove_node("a") # return Exception: Node with data 'a' not found

# Get an element with index (not negative)
llist6 = LinkedList(['a', 'b', 'c'])
print(llist6.get_an_element(1)) # return b
print(llist6.get_an_element(3)) # return Exception: Index is out of range of list

# Reverse the linked list
llist7 = LinkedList(['a', 'b', 'c'])
llist7.reverse()
print(llist7) # return c -> b -> a -> None