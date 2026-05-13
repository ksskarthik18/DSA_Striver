def find_goodnumber(n):

    MOD = 10**9 + 7

    even_count = (n+1)//2
    odd_count = (n)//2

    even_part = power(5,even_count,MOD)
    odd_part = power(4,odd_count,MOD)

    return (even_part * odd_part) % MOD

def power(x,n,mod):
    if n < 0:
        x = 1/x
        n = -n
    
    result = 1
    while n > 0:
        if n%2 == 1:
            result = (result*x) % mod
        
        x = (x * x) % mod
        n = n//2

    return result


def main():
    print(find_goodnumber(4))
main()
