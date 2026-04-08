def linear_search(nums,k):
    n=len(nums)
    for i in range(n):
        if nums[i]==k:
            return i
    
    return -1

def main():
    nums=[2,5,3,7,8,6,9]
    k=2
    print(linear_search(nums,3))
main()