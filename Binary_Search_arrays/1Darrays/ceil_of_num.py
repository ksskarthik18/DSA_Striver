#Time Complexity : O(log n base 2)

def ceil_of_num(nums,target):
    n=len(nums)
    low=0
    high=n-1
    result=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            result=nums[mid]
            high=mid-1
        else:
            low=mid+1
    
    return result

def main():
    nums=[1,2,3,3,5,8,8,10,10,11]
    target=9
    print(ceil_of_num(nums,target))
main()