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
    
    def swap_pairs(self):
        if self.head is None:
            return None
        dummy1 = Node(0)
        dummy1.next = self.head
        self.head.prev = dummy1
        dum1 = dummy1
        current = self.head

        while current and current.next:
            first = current
            second = current.next

            new_pair = second.next
            dum1.next = second
            second.prev = dum1

            second.next = first
            first.prev = second

            first.next = new_pair
            if new_pair:
                new_pair.prev = first
            
            dum1 = first
            current = new_pair

        self.head =dummy1.next
        self.head.prev = None
        return self.head

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
# my_doubly_linked_list.append(3)
my_doubly_linked_list.head = my_doubly_linked_list.swap_pairs()
my_doubly_linked_list.print_list()
