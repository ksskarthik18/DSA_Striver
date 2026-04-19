def find_sqrt_num(n):
    low=1
    high = n
    res=None
    while low<=high:
        mid = (low+high)//2
        if mid * mid <= n:
            res=mid
            low=mid+1
        else:
            high=mid-1

    return res

def main():
    print(find_sqrt_num(38))

main()
