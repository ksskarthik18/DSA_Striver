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
    
    def add_two_LL(self,head1,head2):
        L1 = head1
        L2 = head2
        dummy1 = Node(-1)
        dum1 = dummy1

        carry =0
        while L1 is not None or L2 is not None or carry:
            sum1 =0
            if L1 is not None:
                sum1+=L1.value
                L1=L1.next
            if L2 is not None:
                sum1+=L2.value
                L2=L2.next
            sum1+=carry
            carry = sum1//10
            new_node = Node(sum1%10)
            dum1.next = new_node
            dum1 = dum1.next
        
        return dummy1.next
    
def main():
    #list1
    head1 = Node(2)
    head1.next = Node(4)
    head1.next.next = Node(3)


    #list2
    head2 = Node(5)
    head2.next = Node(6)
    head2.next.next = Node(4)

    my_linked_list = LinkedList(-1)
    my_linked_list.head = my_linked_list.add_two_LL(head1,head2)

    my_linked_list.print_list()

main()
            
