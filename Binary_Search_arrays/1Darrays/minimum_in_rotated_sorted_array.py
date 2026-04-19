#Time complexity : O(log n base 2)

def get_minimum(nums):
    n = len(nums)
    low = 0
    high = n -1
    res= float('inf')
    while low<=high:
        mid=(low+high)//2
        if nums[low]<=nums[mid]:
            res=min(res,nums[low])
            low=mid+1
        else:
            res=min(res,nums[mid])
            high = mid - 1
    
    return res

            

def main():
    nums = [3,4,5,1,2,3]
    print(get_minimum(nums))
main()