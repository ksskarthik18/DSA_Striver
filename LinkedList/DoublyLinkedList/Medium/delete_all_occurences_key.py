#Time Complexity : O(n)
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
    
    def delete_occurences(self,key):
        if self.head is None:
            return None
        
        temp = self.head

        while temp:
            if temp.value == key:
                if temp is self.head:
                    self.head = temp.next
                    self.head.prev = None
                next_node = temp.next
                prev_node = temp.prev

                if next_node:
                    next_node.prev = prev_node
                if prev_node:
                    prev_node.next = next_node
            
                temp = next_node
            else:
                temp = temp.next

        return self.head
    
my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(3)

my_doubly_linked_list.head = my_doubly_linked_list.delete_occurences(3)

my_doubly_linked_list.print_list()
