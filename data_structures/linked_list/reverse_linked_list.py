# Reverse a given Linked List


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
            print print_val.data
            print_val = print_val.next_node

    # Prepend - Inserting at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev


linked_list = LinkedList()
print "**********************"
print "Creating a linked List"
linked_list.prepend("Mon")
linked_list.prepend("Tues")
linked_list.prepend(10)
linked_list.list_print()
print "**********************"
linked_list.reverse()
print "Reversed Linked List"
linked_list.list_print()


