
#Time Complexity : O(N X (max-min+1))
def possible(nums,day,m,k):
    cnt=0
    no_of_boquets=0
    n=len(nums)
    for i in range(n):
        if nums[i]<= day:
            cnt+=1
        else:
            no_of_boquets+=cnt/k
            cnt=0
    no_of_boquets += (cnt/k)

    if no_of_boquets>=m:
        return True
    else:
        return False



def min_days(nums,m,k):
    n=len(nums)
    low = min(nums)
    high = max(nums)
    ans=-1
    while low<=high:
        mid = (low+high)//2
        if (possible(nums,mid,m,k)==True):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def main():
   
   bloomDay = [1,10,3,10,2]
   m = 3
   k = 2
   print(min_days(bloomDay,m,k))
main()