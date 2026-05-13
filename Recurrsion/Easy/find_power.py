def find_power(x,n):
    if n< 0:
        x = 1/x
        n = -1
    result = 1
    while n > 0:
        if n%2 == 1:
            result = result * x
        x = x*x
        n = n//2
    return result

def main():
    result=find_power(2,6)
    print(result)
main()