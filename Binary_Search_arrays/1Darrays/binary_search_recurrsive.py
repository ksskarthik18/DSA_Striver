#Time Complexity : O(log n base 2)

def binary_search_recurrsive(nums,low,high,target):
    if low>high:
        return -1
    mid = low + ((high-low)//2)
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        return binary_search_recurrsive(nums,low,mid-1,target)
    else:
        return binary_search_recurrsive(nums,mid+1,high,target)

def main():
    nums=[3,4,6,7,9,12,16,17]
    target=9
    n=len(nums)
    print(binary_search_recurrsive(nums,0,n-1,target))

main()