
def insert_sorted(stack,value):
    if len(stack) == 0 or stack[-1]<=value:
        stack.append(value)
        return
    
    temp = stack.pop()
    insert_sorted(stack,value)
    stack.append(temp)


def sort_a_stack(stack):
    if len(stack) <= 1:
        return
    temp = stack.pop()
    sort_a_stack(stack)
    insert_sorted(stack,temp)


def main():
    stack = [4,2,5,1]
    print("Original stack")
    print(stack)

    sort_a_stack(stack)
    print("\nSorted stack :")
    print(stack)
main()



    