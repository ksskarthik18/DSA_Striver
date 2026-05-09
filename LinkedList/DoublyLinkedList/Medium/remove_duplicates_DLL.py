#Time Complexity : O(2n)

class Node:
    def __init__(self,value):
        self.value =value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True
    
    # def remove_duplicates(self):
    #     if self.head is None:
    #         return None
    #     dummy1 = Node(-1)
    #     dum1 = dummy1

    #     temp = self.head
    #     prev_value = None
    #     while temp:
    #         new_node = Node(temp.value)
    #         if prev_value != temp.value:
    #             new_node = Node(temp.value)
    #             dum1.next = new_node
    #             new_node.prev = dum1
    #             dum1 = dum1.next
    #             prev_value = temp.value
    #         temp=temp.next

    #     self.head = dummy1.next
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next

    #     self.tail = temp
    #     return self.head

    def remove_duplicates(self):
        if self.head is None:
            return None
        current = self.head
        while current and current.next:
            if current.value == current.next.value:
                duplicate = current.next
                current.next = duplicate.next

                if duplicate.next:
                    duplicate.next.prev = current
                else:
                    self.tail = current
            
            else:
                current = current.next
        
        return self.head

            



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


my_doubly_linked_list.head = my_doubly_linked_list.remove_duplicates()
my_doubly_linked_list.print_list()
