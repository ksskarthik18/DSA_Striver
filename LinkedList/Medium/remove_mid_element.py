#Time Complexity : O (N/2)

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
    

    def remove_mid(self):
        if not self.head or not self.head.next:
            return None
        slow = self.head
        fast = self.head
        #fast = self.head.next.next

        prev =None
        while fast and fast.next:
            prev=slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        slow.next = None


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.remove_mid()
my_linked_list.print_list()