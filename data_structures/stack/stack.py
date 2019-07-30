# Implement a stack


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
print "Is stack empty?", s.is_empty()

print "Appending to stack"
s.push(4)       # 1
print s.peek()

s.push('dog')   # 2
print s.peek()

s.push(True)    # 3
print s.peek()

s.push(8.4)     # 4
print s.peek()
print "*************************"
print "Size:", s.size()
print "*************************"
print "Removing items from stack"
print s.pop()   # Top most element on the stack
print s.pop()   # Next element on the stack
print "*************************"
print "Size:", s.size()
