#Time complexity : O(N x 2M)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.child = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print_list(self,head):
        temp = head
        while temp is not None:
            print(temp.value)
            temp=temp.child
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    def merge_two_list(self,list1,list2):
        dummy1 = Node(-1)
        res = dummy1
        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
        
        if list1:
            res.child = list1
        else :
            res.child = list2
        
        return dummy1.child

      
    def flatten_list(self,head):
        if head == None or head.next == None:
            return head
        merged_head = self.flatten_list(head.next)
        return self.merge_two_list(head,merged_head)


ll = LinkedList(-1)

# Level 1
head = Node(1)
head.next = Node(4)
head.next.next = Node(7)

# Child list for 1
head.child = Node(2)
head.child.child = Node(3)

# Child list for 4
head.next.child = Node(5)
head.next.child.child = Node(6)

# Child list for 7
head.next.next.child = Node(8)
head.next.next.child.child = Node(9)

# Flatten
flat_head = ll.flatten_list(head)

# Print
ll.print_list(flat_head)