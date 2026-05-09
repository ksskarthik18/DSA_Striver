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
    
    def find_middle(self,head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev
    
    def merge_sorted_arrays(self,L1,L2):
        dummy = Node(0)
        temp = dummy
        while L1 and L2:
            if L1.value < L2.value:
                temp.next = L1
                L1 =L1.next
            else:
                temp.next = L2
                L2 = L2.next
            temp = temp.next
        if L1:
            temp.next = L1
        else:
            temp.next = L2

        return dummy.next
    
    def sortLL(self,head):
        if head is None or head.next is None:
            return head
        middle = self.find_middle(head)
        left_head = head
        right_head = middle.next
        middle.next = None

        left_head=self.sortLL(left_head)
        right_head = self.sortLL(right_head)
        return self.merge_sorted_arrays(left_head,right_head)




my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(1)


my_linked_list.head = my_linked_list.sortLL(my_linked_list.head)

my_linked_list.print_list()

