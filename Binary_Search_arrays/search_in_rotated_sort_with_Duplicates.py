# Time Complexity :  O(log n)
# Worst Case : O(n)

def search_num(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        if nums[low]==nums[mid] and nums[mid]==nums[high]:
            low+=1
            high-=1

        elif nums[low]<= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high-=1
            else:
                low+=1
        else:
            if nums[mid]< target <= nums[high]:
                low+=1
            else:
                high-=1
    
    return -1
        


def main():
    nums = [3,1,2,3,3,3,3]
    target = 3
    print(search_num(nums,target))
main()