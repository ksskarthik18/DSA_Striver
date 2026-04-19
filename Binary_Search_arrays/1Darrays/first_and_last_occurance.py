#Time Complexity : O(log n) + O(log n) = O(log n)

def first(nums,target):
    n=len(nums)
    low=0
    high=n-1
    first=-1
    while low<= high:
        mid = (low+high)//2
        if nums[mid] == target:
            first=mid
            high = mid -1
        elif nums[mid] < target:
            low = mid + 1
        else :
            high = mid -1
    
    return first

def last(nums,target):
    n=len(nums)
    low=0
    high=n-1
    last=-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            last=mid
            low = mid + 1
        elif nums[mid]> target :
            high= mid - 1
        else :
            low = mid + 1
    return last

def main():
    nums = [5,7,7,8,8,10]
    target = 8
    fst=first(nums,target)
    if fst == -1:
        print([-1,-1])
    else :
        lst=last(nums,target)
        print([fst,lst])
main()

