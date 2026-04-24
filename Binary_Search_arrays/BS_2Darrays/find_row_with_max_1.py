# Time Complexity : O(n x log n base 2)
def lowerBound(nums,target):
    n=len(nums)
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            ans=mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

def find_row_max1(nums,n,m):
    cnt_max=0
    index = -1
    for i in range(n):
        cnt_ones= m - lowerBound(nums[i],1)
        if (cnt_ones > cnt_max):
            cnt_max = cnt_ones
            index = i

    return index

def main():
    nums=[[1,1,1],[0,0,1],[0,0,0]]
    n = 3
    m = 3
    print(find_row_max1(nums,3,3))
main()