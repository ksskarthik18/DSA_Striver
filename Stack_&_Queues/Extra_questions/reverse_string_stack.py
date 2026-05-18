class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
def reverse_string(word):
    s = Stack()
    for ch in word:
        s.push(ch)
    
    result=""
    while not s.isEmpty():
        result += s.pop()
    return result

def main():
    word = "hello"
    print(reverse_string(word))
main()
