def find_times_rotated(nums):
    n=len(nums)
    low=0
    high=n-1
    res=float('inf')
    inx = -1
    while low<high:
        mid = (low+high)//2
        if nums[mid]<nums[high]:
            high=mid
        elif nums[mid]>nums[high]:
            low = mid + 1
        else:
            high-=1
    return low


def main():
    nums = [3,4,5,1,2]
    print(find_times_rotated(nums))
main()