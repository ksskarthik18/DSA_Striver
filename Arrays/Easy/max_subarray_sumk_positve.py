def length_positive_subarray(nums,k):
    left=0
    curr_sum=0
    max_len=0

    for right in range(len(nums)):
        curr_sum += nums[right]

        if curr_sum > k :
            curr_sum -= nums[left]
            left += 1

        if curr_sum == k:
            max_len = max(max_len,right-left +1)
    
    return max_len


    
def main():

    nums=[1,2,3,0,1,1,1,1,3,3]
    k=3
    # nums = [1, -1, 5, -2, 3]
    # k = 3
    print(length_positive_subarray(nums,k))

main()