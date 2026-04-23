import math
def required_stations(nums,dist,k):
    n=len(nums)
    cnt_stations = 0
    for i in range(1,n):
        gap = nums[i]-nums[i-1]
        cnt_stations += math.ceil(gap/dist)-1
    if cnt_stations >= k:
        return True
    else:
        return False


def minimise_gas_distance(nums,k):
    nums.sort()
    low = 1e-6
    high = max(nums)-min(nums)
    ans=-1
    while high - low > 1e-6:
        mid = (low + high)/2
        if required_stations(nums,mid,k) == True:
            low = mid
        else:
            ans = mid
            high = mid
    return ans

    

def main():
    nums=[1,2,3,4,5]
    k=4
    print(minimise_gas_distance(nums,k))
main()




