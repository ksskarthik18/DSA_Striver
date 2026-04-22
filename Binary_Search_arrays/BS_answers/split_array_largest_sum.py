def find_sum(nums,split,k):
    t_sum=0
    cnt=1
    for num in nums:
        t_sum +=num
        if t_sum > split:
            t_sum=num
            cnt+=1
    
    if cnt>k:
        return True
    return False



def split_array_largest_Sum(nums,k):
    n = len(nums)
    low = max(nums)
    high = sum(nums)

    while low <= high:
        mid = (low+high)//2
        if find_sum(nums,mid,k)== True:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

def main():
    nums = [7,2,5,10,8]
    k = 2
    print(split_array_largest_Sum(nums,k))

main()

