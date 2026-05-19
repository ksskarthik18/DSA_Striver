# enqueue() → O(1)
# dequeue() → O(n)
# front()   → O(1)
# isEmpty() → O(1)
class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue underflow"
        
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return -1
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

def main():

    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front:", q.front())

    print("Dequeue:", q.dequeue())

    print("Front:", q.front())
main()
