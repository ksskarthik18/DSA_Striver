def binary_search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    
    return -1

def main():
    nums=[3,4,6,7,9,12,16,17]
    target=9
    print(binary_search(nums,target))

main()
