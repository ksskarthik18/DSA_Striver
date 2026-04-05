def fib(n):
    if n<=1:
        return n
    a=0
    b=1

    for i in range(2,n+1):
        curr=a+b
        a=b
        b=curr
    return b

print(fib(10))

