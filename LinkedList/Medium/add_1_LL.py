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
    
    def helper_1(self,head):
        temp = head
        if temp is None:
            return 1
        while temp:
            carry = self.helper_1(temp.next)
            temp.value= temp.value + carry
            if temp.value < 10:
                return 0
            temp.value = 0
            return 1
    
    def add_1(self,head):
        carry= self.helper_1(head)
        if carry == 1:
            new_node = Node(1)
            new_node.next = head
        return new_node
    

def main():
    my_linked_list = LinkedList(9)
    my_linked_list.append(9)
    my_linked_list.append(9)
    my_linked_list.append(9)

    my_linked_list.head = my_linked_list.add_1(my_linked_list.head)
    my_linked_list.print_list()
main()
        

    
    