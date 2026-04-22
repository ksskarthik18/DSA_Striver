def find_maximum_time(painters,time,nums,mid):
    n=len(nums)
    cnt=1
    t_time=0
    for num in nums:
        t_time +=num
        if t_time > mid :
            t_time = mid
            cnt+=1
    
    if cnt > painters:
        return True
    else :
        return False








def painter_parition(painters,time,nums):
    n=len(nums)
    low = max(nums)
    high = sum(nums)
    while low<=high:
        mid = (low + high)//2
        if (find_maximum_time(painters,time,nums,mid) == True):
            low = mid + 1
        else :
            high = mid - 1
    
    return low*time

def main():
    painters= 2
    time = 5
    nums=[1,10]
    print(painter_parition(painters,time,nums))

main()
