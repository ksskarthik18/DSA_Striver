def floor_of_num(nums,target):
    n=len(nums)
    low=0
    high=n-1
    result=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=target:
            result=nums[mid]
            low=mid+1
        else:
            high=mid-1
    
    return result
def main():
    nums=[1,2,3,3,5,8,8,10,10,11]
    target=6
    print(floor_of_num(nums,target))
main()
