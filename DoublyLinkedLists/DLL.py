class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        to_delete = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            to_delete.prev = None
        self.length -= 1
        return to_delete
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        to_delete = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            to_delete.next = None
        
        self.length -= 1
        return to_delete
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-index-1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-index-1):
                temp = temp.prev
        temp.value = value
    
    def insert(self, index ,value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length-1:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            after = temp.next
            new_node.next = after
            new_node.prev = temp
            after.prev = new_node
            temp.next = new_node
            self.length += 1

    def reverse(self):
        curr = self.head
        temp = None

        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp:
            self.head, self.tail = self.tail, self.head

