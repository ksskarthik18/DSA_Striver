import math
def get_sum(nums,mid):
    total_sum=0
    for num in nums:
        total_sum += math.ceil((num+mid-1)//mid)
    return total_sum

def smallest_divisort_threshold(nums,threshold):
    low = 1
    high=max(nums)
    while low<=high:
        mid = (low+high)//2
        t_sum=get_sum(nums,mid)
        if t_sum <= threshold:
            high = mid - 1
        else:
            low = mid + 1

    return low

def main():
    nums = [44,22,33,11,1]
    threshold = 5
    print(smallest_divisort_threshold(nums,threshold))
main()

