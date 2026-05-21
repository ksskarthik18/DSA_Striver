#Time Complexity : O(3N) 
def trapping_rainwater(nums):
    n = len(nums)
    total = 0
    left_max = prefix_max(nums,n)
    right_max = suffix_max(nums,n)
    for i in range(n):

        if left_max[i] > nums[i] and right_max[i] > nums[i]:
            total += min(left_max[i],right_max[i]) - nums[i]
    return total

def prefix_max(nums,n):
    prefix = [0]*n
    prefix[0] = nums[0]
    for i in range(1,n):
        prefix[i] = max(prefix[i-1],nums[i])
    return prefix

def suffix_max(nums,n):
    suffix = [0]*n

    suffix[n-1] = nums[n-1]
    for i in range(n-2,-1,-1):
        suffix[i] = max(suffix[i+1],nums[i])
    return suffix

def main():

    nums=[4,2,0,3,2,5]

    print(trapping_rainwater(nums))

main()
