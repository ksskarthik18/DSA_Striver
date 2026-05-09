class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def binary_to_decimal(self):
        current = self.head
        result = 0

        while current:
            result = result * 2 + current.value
            current = current.next

        return result


# Test 1: 101 → 5
ll = LinkedList(1)
ll.append(0)
ll.append(1)
print(ll.binary_to_decimal())  # 5

# Test 2: 1101 → 13
ll = LinkedList(1)
ll.append(1)
ll.append(0)
ll.append(1)
print(ll.binary_to_decimal())  # 13