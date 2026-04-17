def lower_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    result=n
    while low<= high:
        mid = (low + high)//2
        if nums[mid]>=target:
            result=mid
            high = mid-1
        else:
            low = mid + 1
    return result

def upper_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    result=n
    while low<= high:
        mid = (low + high)//2
        if nums[mid]>target:
            result=mid
            high = mid-1
        else:
            low = mid + 1
    return result\
    
def first_and_last_occur(nums,target):
    n = len(nums)
    lb=lower_bound(nums,target)
    if nums[lb] == n or nums[lb]!=target:
        return [-1,-1]
    return [lb,upper_bound(nums,target)-1]

def main():
    nums = [5,7,7,8,8,10]
    target=8
    print(first_and_last_occur(nums,target))
main()
