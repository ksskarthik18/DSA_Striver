class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    def pop(self):
        if self.length==0:
            return None
        pre = self.head
        temp = pre
        while temp.next is not None:
            pre = temp
            temp=temp.next
        self.tail = pre
        self.tail.next=None
        self.length-=1
        if self.length == 0:
            self.tail =None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length-=1

        if self.length==0:
            self.tail = None
        return temp
    
    def get(self,index):
        if index < 0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp =temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index >self.length:
            return False
        if index==0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index < 0 or index >self.length:
            return None
        if index==0:
            return self.pop_first()
        if index == self.length-1:
            return self.append()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length-=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
    def search(self,value):
        if self.length == 0:
            return False
        temp = self.head
        while temp.next:
            if temp.value == value:
                return True
            temp = temp.next
        return False

my_linked_list = LinkedList(4)

my_linked_list.prepend(2)
my_linked_list.append(3)
my_linked_list.print_list()

print('After setting')
my_linked_list.set_value(1,6)
print('Get :')

print(my_linked_list.get(1).value)


my_linked_list.insert(1,8)
print('After inserting')

my_linked_list.print_list()

print('After removing :')
print(my_linked_list.remove(1).value)

print('After removing entire list :')
my_linked_list.print_list()

print('Reversing the entire list :')
my_linked_list.reverse()
my_linked_list.print_list()

print('Search : ')
print(my_linked_list.search(18))






print("Pop :")
print(my_linked_list.pop().value)
print("Pop first :")
print(my_linked_list.pop_first().value)


