#Time Complexity: O(N)
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
    def sort_0_1_2(self,head):
        dummy0 = Node(-1)
        dummy1 = Node(-1)
        dummy2 = Node(-1)

        dum0 = dummy0
        dum1 = dummy1
        dum2 = dummy2
        temp = head

        while temp:
            if temp is None:
                return None
            if temp.value == 0:
                dum0.next = temp
                dum0 = dum0.next
            elif temp.value == 1:
                dum1.next = temp
                dum1 = dum1.next
            elif temp.value == 2 :
                dum2.next = temp
                dum2 = dum2.next
            temp = temp.next
        dum0.next= dummy1.next if dummy1.next else dummy2.next
        dum1.next = dummy2.next
        dum2.next = None

        return dummy0.next



my_linked_list = LinkedList(-1)
# my_linked_list.append(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(0)
# my_linked_list.append(2)
# my_linked_list.append(1)

my_linked_list.head = my_linked_list.sort_0_1_2(my_linked_list.head)
my_linked_list.print_list()

