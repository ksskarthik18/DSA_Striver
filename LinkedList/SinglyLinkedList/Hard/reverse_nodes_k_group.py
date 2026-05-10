
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
    
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def reverse_nodes(self,k):
        if self.head is None:
            return None
        dummy1 = Node(-1)
        dummy1.next =self.head
        previous_group = dummy1

        curr= self.head

        while curr:
            start = curr
            cnt=1

            while cnt<k and curr:
                curr = curr.next
                cnt+=1

            if curr is None :
                break
            next_node = curr.next
            curr.next = None

            new_head = self.reverse(start) 
            previous_group.next = new_head

            start.next = next_node
            previous_group = start
            curr = next_node
        self.head = dummy1.next          
        return self.head
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)
my_linked_list.head = my_linked_list.reverse_nodes(3)
my_linked_list.print_list()
        





