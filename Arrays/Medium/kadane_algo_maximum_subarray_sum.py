def maximum_subarray_sum(nums):
    maxi=nums[0]
    sum1=0

    for i in range(len(nums)):
        sum1+=nums[i]

        if sum1>maxi:
            maxi=sum1
        if sum1 < 0:
            sum1=0
    
    return maxi

def main():
    nums= [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_subarray_sum(nums))
main()