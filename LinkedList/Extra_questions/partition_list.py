#Time Complextiy : O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True 
    def partition_list(self,x):
        if self.head is None:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)

        dum1 = dummy1
        dum2 = dummy2

        current = self.head

        while current:
            if current.value < x :
                dum1.next =current
                dum1 = dum1.next
            else:
                dum2.next = current
                dum2 = dum2.next
            current = current.next

        dum2.next = None

        dum1.next = dummy2.next

        self.head = dummy1.next


my_linked_list = LinkedList(9)
my_linked_list.append(10)
my_linked_list.append(11)
my_linked_list.append(1)
my_linked_list.append(5)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(2)

my_linked_list.partition_list(5)
my_linked_list.print_list()


