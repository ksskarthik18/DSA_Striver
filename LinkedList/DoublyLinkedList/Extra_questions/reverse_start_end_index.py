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
    
    def reverse_btwn(self,start_index,end_index):
        if self.head is None or start_index == end_index:
            return self.head
        dummy1 = Node(0)
        dummy1.next = self.head
        self.head.prev = dummy1
        dum1 = dummy1
        current = self.head
        for _ in range(start_index):
            current = current.next
        
        previous = current.prev
        for _ in range(end_index - start_index):
            to_move = current.next
            current.next = to_move.next
            if to_move.next:
                to_move.next.prev = current
            
            to_move.next = previous.next
            previous.next.prev = to_move

            previous.next = to_move
            to_move.prev = previous
        
        self.head = dummy1.next
        self.head.prev = None

        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp

        return self.head

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

my_doubly_linked_list.head = my_doubly_linked_list.reverse_btwn(1,3)
my_doubly_linked_list.print_list()