class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,value):
        self.stack1.append(value)
    
    def dequeue(self):
        if not self.stack2:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
    
        return self.stack2.pop()
    
    def front(self):
        if self.isEmpty():
            return -1
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]
    
    def isEmpty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

def main():

    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front:", q.front())

    print("Dequeue:", q.dequeue())

    print("Front:", q.front())


main()