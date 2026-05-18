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

def check_parenthesis(paren):
    s = Stack()
    for b in paren:
        if b == "(":
            s.push(b)
        if b == ")":
            if s.isEmpty():
                return False
            s.pop()
    
    return s.isEmpty()
    
def main():
    print(check_parenthesis("((()))"))
    print(check_parenthesis("()(("))
    print(check_parenthesis(")("))
main()
