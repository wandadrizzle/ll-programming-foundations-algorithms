# Example file for Programming Foundations: Algorithms by Joe Marini
# Linked list example


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data): #We're only inserting at the head, 
        # TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def insertAt(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            pass
            tempIdx = 0
            tempNode = self.head
            while tempIdx < index - 1:
                tempNode = tempNode.get_next()
                tempIdx += 1
            new_node.set_next(tempNode.get_next())
            tempNode.set_next(new_node)
        self.count += 1

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head
        while (item is not None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            tempNode = self.head
            while tempIdx < idx - 1:
                tempNode = tempNode.get_next()
                tempIdx += 1
            tempNode.set_next(tempNode.get_next().get_next())
        self.count -= 1


    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list() #Printing out the List

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
print("\nItem count: ", itemlist.get_count())
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()

print("I'm trying to insert an element at a specific index:")
itemlist.insertAt(300, 1)
itemlist.dump_list()