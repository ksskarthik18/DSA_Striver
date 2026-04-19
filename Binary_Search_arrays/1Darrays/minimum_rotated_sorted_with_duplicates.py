def find_minimum_with_duplicates(nums):
    n = len(nums)
    low = 0
    high = n -1
    res=float('inf')
    while low<high:
        mid = (low + high)//2
            
        if nums[mid]<nums[high]:
            high = mid
        elif nums[mid]>nums[high]:
            low=mid+1
        else:
            high-=1

    return nums[low]

def main():
    nums = [3,3,4,5,1,2,3]
    print(find_minimum_with_duplicates(nums))
main()
