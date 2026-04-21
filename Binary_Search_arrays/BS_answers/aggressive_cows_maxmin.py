#Time Complexity : O(nlogn) + [O(log n base 2) x O(N)]

def canWePlaceCows(nums,dist,cows):
    n=len(nums)
    cnt_cows = 1
    last = nums[0]
    for i in range(1,n):
        if nums[i]-last >=dist:
            cnt_cows+=1
            last =  nums[i]

    if cnt_cows >= cows :
        return True
    return False
    


def find_maxPos(nums,cows):
    n= len(nums)
    nums.sort()
    low = 0
    high = max(nums)-min(nums)
    ans=-1
    while low<=high:
        mid = (low + high)//2
        if canWePlaceCows(nums,mid,cows) == True:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def main():
    nums=[0,3,4,7,10,9]
    cows=4
    print(find_maxPos(nums,cows))
main()