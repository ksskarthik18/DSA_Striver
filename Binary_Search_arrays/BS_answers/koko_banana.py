#Time Complexity : O(N) * O(log max_element base 2)
import math
def hours(nums,speed):
    n=len(nums)
    total_hours=0
    for i in range(n):
        total_hours += math.ceil((nums[i]+speed-1)/speed)
    return total_hours

def num_bananas(nums,h):
    n = len(nums)
    low = 1
    high = max(nums)
    result=None
    while low<= high:
        mid = (low+high)//2
        t_hrs=hours(nums,mid)
        if t_hrs <=h:
            result=mid
            high = mid - 1
            
        else:
            low = mid + 1
            
    return result

def main():
    piles = [3,6,7,11]
    h=8
    print(num_bananas(piles,h))
main()
