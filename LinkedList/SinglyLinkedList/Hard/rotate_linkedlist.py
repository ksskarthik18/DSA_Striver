#Time Complexity : O(2N)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    def rotate_LL(self,k):
        if self.head is None or self.head.next is None:
            return self.head
        tail = self.head
        length=0
        while tail.next:
            length+=1
            tail = tail.next
        length+=1
        if k%length == 0:
            return self.head
        else:
            shift = length - (k%length) - 1
            curr = self.head
            for _ in range(shift):
                curr = curr.next
            
            new_head = curr.next
            curr.next = None
            tail.next = self.head
        
        self.head = new_head
        return self.head

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.append(5)
my_linked_list.head = my_linked_list.rotate_LL(2)
my_linked_list.print_list()

        
