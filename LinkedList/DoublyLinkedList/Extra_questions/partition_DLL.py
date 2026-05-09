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
    

    def partition_list(self,x):
        if self.head is None:
            return None
        dummy1 = Node(-1)
        dummy2 = Node(-1)
        dum1 = dummy1
        dum2 = dummy2
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            current.prev = None
            if current.value < x:
                dum1.next = current
                current.prev = dum1

                dum1 = dum1.next
            else:
                dum2.next = current
                current.prev = dum2
                dum2 = dum2.next
            current  = next_node        
        dum1.next = dummy2.next

        if dummy2.next:
            dummy2.next.prev = dum1
        self.head = dummy1.next

        if self.head:
            self.head.prev = None
        
        self.tail = dum2 if dummy2.next else dum1

        if self.tail:
            self.tail.next =None
        
        return self.head


my_doubly_linked_list = DoublyLinkedList(9)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

my_doubly_linked_list.head = my_doubly_linked_list.partition_list(4)
my_doubly_linked_list.print_list()
    