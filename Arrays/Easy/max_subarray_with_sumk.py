def longest_subarray_sumk(nums,k):
    prefix_sum=0
    max_len=0
    hashmap={}

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == k:
            max_len=i+1
        
        if prefix_sum - k in hashmap :
            length = i - hashmap[prefix_sum - k]
            max_len = max(max_len,length)
        
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i
        
    return max_len
    

def main():
    nums=[1,2,3,0,1,1,1,1,3,3]
    k=3
    # nums = [1, -1, 5, -2, 3]
    # k = 3
    print(longest_subarray_sumk(nums,k))

main()