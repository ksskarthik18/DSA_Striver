def insert_at_bottom(stack,value):
    if len(stack) == 0:
        stack.append(value)
        return
    temp = stack.pop()
    insert_at_bottom(stack,value)
    stack.append(temp)



def reverse_stack(stack):
    if len(stack) <=1:
        return
    
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack,temp)

def main():
    stack = [1,2,3,4]
    print("Original stack")
    print(stack)

    reverse_stack(stack)
    print("\nReversed stack :")
    print(stack)
main()