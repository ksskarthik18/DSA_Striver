#Time Complexity : O(N + k)
def remove_digits(s,k):
    stack=[]
    for ch in s:
        while len(stack)!=0 and k > 0 and (stack[-1]) > ch:
            stack.pop()
            k-=1
        stack.append(ch)
    
    while k > 0 :
        stack.pop()
        k-=1
    result = "".join(stack)
    #For removing leading zeroes
    result  = result.lstrip('0')
    return result if result else '0'
    
def main():
    num = "1432219"
    k = 3
    print(remove_digits(num,k))
main()
