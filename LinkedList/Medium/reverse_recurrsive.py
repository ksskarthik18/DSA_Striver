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


    def reverse_recurssive(self,head):
        if head is None or head.next is None:
            return head
        new_head = self.reverse_recurssive(head.next)

        front = head.next
        front.next = head
        head.next = None
        return new_head
    
    def reverse(self):
        if self.head is None:
            return
        self.tail = self.head
        self.head = self.reverse_recurssive(self.head)
         


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print("Before reverse:")
my_linked_list.print_list()

my_linked_list.reverse()
print("\nAfter reverse:")
my_linked_list.print_list()