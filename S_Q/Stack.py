class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if not self.top:
            return None
        to_pop = self.top
        self.top = self.top.next
        to_pop.next = None
        self.height -= 1
        return to_pop



myStack = Stack(3)
myStack.push(10)
myStack.print_stack()

print(myStack.pop())