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
    
    def find_pairs(self,x):
        if self.head is None:
            return None

        left = self.head
        right = self.tail
        list1 = []
        while left.value < right.value:
            if (left.value + right.value) > x:
                right = right.prev
            elif left.value + right.value < x:
                left = left.next
            else:
                list1.append((left.value,right.value))
                left = left.next
                right = right.prev

        return list1
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(9)

print(my_doubly_linked_list.find_pairs(5))

        
