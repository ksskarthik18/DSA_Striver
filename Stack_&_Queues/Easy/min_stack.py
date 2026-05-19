#Time Complexity : O(1)
class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self,value):
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        
        else:
            self.min_stack.append(min(value,self.min_stack[-1]))
    
    def pop(self):
        if self.empty():
            return "Stack Underflow"
        self.min_stack.pop()
        return self.stack.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return len(self.stack) == 0
    def get_min(self):
        return self.min_stack[-1]
    
def main():
    s = Stack()

    s.push(10)
    s.push(2)
    s.push(30)
    s.push(1)

    print("Top:", s.top())

    print("Minimum :", s.get_min())

    print("Pop:", s.pop())

    print("Top:", s.top())

    print("Minimum :", s.get_min())
main()
