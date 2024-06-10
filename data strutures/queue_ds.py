class Node:
    def __init__(self, data:str):
        self.data = data
        self.next = None

    '''def __repr__(self):
        return self.data'''

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            new_item = Node(value)
            print("Adding", new_item.data, "to the queue!")
            if self.get_size() == 0:
                self.head = new_item
                self.tail = new_item
            elif self.get_size() == 1:
                self.tail = new_item
                self.head.next = self.tail
            else:
                self.tail.next = new_item
                self.tail = new_item
        else:
            print("Sorry, no more rooms!")

        self.size += 1

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(item_to_remove.data + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
        else:
            print("The queue is totally empty!")

    def peek(self):
        if self.size > 0:
            return self.head.data
        else:
            print("No orders waiting!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.get_size() > 9:
            return False
        return True

print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue()
print("Adding orders to our deli line...\n------------")

deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# deli_line.enqueue("western omelet with home fries")

print("------------\n Our first order will be " + deli_line.peek())
print("------------\n Now serving...\n------------")

deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()