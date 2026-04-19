#Time Complexity :O(log n)
def find_nroot_num(n,m):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        if pow(mid,n) > m:
            high=mid-1
        elif pow(mid,n)<m:
            low=mid+1
        else:
            return mid
    return -1

def main():
    print(find_nroot_num(4,81))
main()

    
