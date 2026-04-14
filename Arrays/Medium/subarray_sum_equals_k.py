def subarray_sum_equals_k(nums,k):
    map1={0:1}
    pre_sum=0
    count=0

    for num in nums:
        pre_sum+=num
        remove=pre_sum-k

        if remove in map1:
            count+=map1[remove]
        
        map1[pre_sum]=map1.get(pre_sum,0)+1
    return count

def main():
    nums = [1,2,3] 
    k = 3
    print(subarray_sum_equals_k(nums,k))
main()