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
    
def main():
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print("Top:", s.top())

    print("Pop:", s.pop())

    print("Top:", s.top())

    print("Size:", s.size())
main()