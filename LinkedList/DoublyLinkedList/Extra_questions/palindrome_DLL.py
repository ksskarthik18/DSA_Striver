class Node:
    def __init__(self,value):
        self.value =value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True
    
    def palindrome(self):
        if self.length == 0:
            return True
        if self.length == 1:
            return True
        forward = self.head
        backward = self.tail
        while forward != backward:
            if forward.value == backward.value:
                forward = forward.next
                backward = backward.prev
            else:
                return False
        
        return True
    
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

print(my_doubly_linked_list.palindrome())
