#Time Complexity : O(n^2)
class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        return self.stack.pop()
    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0
    
def sort_stack(stack):
    additional_stack = Stack()
    
    while not stack.isEmpty():
        temp = stack.pop()

        while not additional_stack.isEmpty() and additional_stack.top() > temp:
            stack.push(additional_stack.pop())
        additional_stack.push(temp)


    while not additional_stack.isEmpty():
        stack.push(additional_stack.pop())

def main():
    s = Stack()
    s.push(4)
    s.push(1)
    s.push(3)
    s.push(2)

    sort_stack(s)
    print("Sorted stack :")
    while not s.isEmpty():
        print(s.pop())
main()