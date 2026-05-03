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
    
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

my_linked_list = LinkedList(3)
my_linked_list.append(2)
my_linked_list.append(0)
my_linked_list.append(-4)
temp = my_linked_list.head
for _ in range(1):
    temp = temp.next
my_linked_list.tail.next = temp
print(my_linked_list.detect_loop())