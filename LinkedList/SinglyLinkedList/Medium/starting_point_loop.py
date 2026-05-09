#Time Complexity : O(n)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def detect_start_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = self.head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next

                return slow.value
        
        return None

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(15)

my_linked_list.append(4)
my_linked_list.append(13)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)

temp = my_linked_list.head
while temp.value!=15:
    temp = temp.next

my_linked_list.tail.next = temp


print(my_linked_list.detect_start_loop())