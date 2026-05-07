#Time Complexity : O(N1+N2)

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
    
    # def find_length(self,head):
    #     temp= head
    #     cnt=0
        
    #     while temp:
    #         cnt+=1
    #         temp = temp.next

    #     return cnt
    

    # def find_point(self,head1,head2):
    #     l1 = self.find_length(head1)
    #     l2 = self.find_length(head2)

    #     temp1 = head1
    #     temp2 = head2
    #     if l1>l2:
    #         diff = l1-l2
    #         for _ in range(diff):
    #             temp1 = temp1.next
    #     else :
    #         diff = l2-l1
    #         for _ in range(diff):
    #             temp2 = temp2.next
    

    #     while temp1 and temp2:
    #         if temp1 != temp2:
    #             temp1 = temp1.next
    #             temp2 = temp2.next
    #         else:
    #             return temp1
    #     return None


    def find_point(self,head1,head2):
        if head1 is None or head2 is None:
            return None
        t1 = head1
        t2 = head2

        while t1!= t2:
            t1 = t1.next
            t2 = t2.next
            if t1 == t2 :
                return t1

            elif t1.next is None:
                t1 = head2

            elif t2.next is None:
                t2 = head1
        return t1


    
def main():
    common = Node(8)
    common.next = Node(10)

    #list1
    head1 = Node(3)
    head1.next = Node(6)
    head1.next.next = Node(9)
    head1.next.next.next = common


    #list2
    head2 = Node(4)
    head2.next = Node(7)
    head2.next.next = common

    L1 = LinkedList(0)
    intersection = L1.find_point(head1,head2)
    if intersection:
        print("Intersection point :",intersection.value)
    else:
        print("No intersection")

main()



        

