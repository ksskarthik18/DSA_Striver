#Time Complexity : O(n**2)
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

    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

my_linked_list = LinkedList(4)

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(6)
my_linked_list.append(4)
my_linked_list.append(9)

my_linked_list.remove_duplicates()
my_linked_list.print_list()


    