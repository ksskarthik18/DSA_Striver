#Time Complexity : O(1)
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
    
    def reverse(self):
        if self.head is None:
            return None
        temp = None
        current = self.head
        while current:
            temp = current.prev

            current.prev = current.next
            current.next = temp

            #move to next node  
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)

my_doubly_linked_list.reverse()
my_doubly_linked_list.print_list()