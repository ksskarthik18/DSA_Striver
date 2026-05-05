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
    

    def odd_even_list(self):
        # odd = Node(0)
        # odd1 = odd
        # even = Node(0)
        # even1 = even
        # current = self.head
        # cnt=1

        # while current:
        #     new_node = current.next
        #     current.next = None
        #     if cnt%2 == 1:
        #         odd1.next = current
        #         odd1 = odd1.next
                
        #     else:
        #         even1.next = current
        #         even1 = even1.next
            
        #     cnt+=1
        #     current = new_node

        # odd1.next = even.next
        # even1.next = None

        if not self.head:
            return None
        
        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.odd_even_list()
my_linked_list.print_list()







