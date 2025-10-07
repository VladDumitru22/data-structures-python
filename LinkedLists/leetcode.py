class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_kth_from_end(self, k):
        if k == 1:
            return self.tail
        slow = self.head
        fast = self.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    def remove_duplicates(self):
        seen = set()
        prev = None
        temp = self.head

        while temp:
            if temp.value in seen:
                prev.next = temp.next
            else:
                seen.add(temp.value)
                prev = temp
            temp = temp.next

    def binary_to_decimal(self):
        digits = []
        decimal = 0

        temp = self.head
        while temp:
            digits.insert(0, temp.value)
            temp = temp.next

        for i in range(len(digits)):
            decimal += digits[i] * (2**i)
        return decimal
    
    def partition(self, x):
        if not self.head:
            return None
        
        dummy1 = Node(0)
        prev1 = dummy1
        dummy2 = Node(0)
        prev2 = dummy2
        temp = self.head
        
        while temp:
            if temp.value < x:
                prev1.next = temp
                prev1 = temp
            elif temp.value >= x:
                prev2.next = temp
                prev2 = temp
            temp = temp.next
        prev1.next = dummy2.next
        prev2.next = None
        self.head = dummy1.next
