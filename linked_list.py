# Implement LinkedList data structure
# LinkedList allows the following operations:
# Insert
# Append
# Prepend
# Delete
# Get(i) -> Gets the ith element


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def list_print(self):
        print_val = self.head
        while print_val is not None:
            print (print_val.data)
            print_val = print_val.next_node

    # Insert - Inserting between two nodes, that is inserts value after position of node specified
    def insert(self, position, data):
        if position is None:
            print "The node is unavailable"
            return
        new_node = Node(data)
        new_node.next_node = position.next_node
        position.next_node = new_node

    # Prepend - Inserting at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Append - Inserting at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    # Delete - Removing a node from the list
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # Get ith position in the linked list
    def get(self, position):
        current = self.head
        count = 0

        while current:
            if count == position:
                return current.get_data()
            count = count + 1
            current = current.next_node
        if current is None:
            raise ValueError("Index not in list")


linked_list = LinkedList()

# Creating a new linked list
linked_list.head = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")

linked_list.head.set_next(e2)
e2.set_next(e3)

# Insert
linked_list.insert(e3, "Thur")

# Prepend
linked_list.prepend("Sun")

# Append
linked_list.append("Fri")
linked_list.list_print()
print "************************"

# Delete
linked_list.delete("Wed")
linked_list.list_print()
print "************************"

# Get the data in the 4th position
data = linked_list.get(4)
print data

