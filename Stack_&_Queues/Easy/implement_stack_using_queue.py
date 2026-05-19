class Stack:
    def __init__(self):
        self.queue = []
    
    def push(self,value):
        self.queue.append(value)

        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
    
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        
        return self.queue.pop(0)
    
    def top(self):
        if self.isEmpty():
            return -1
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

def main():

    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print("Top:",s.top())

    print("Pop:",s.pop())

    print("Top:",s.top())

main()
