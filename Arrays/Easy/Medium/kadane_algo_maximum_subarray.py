def maximum_subarray(nums):
    maxi=nums[0]
    sum1=0
    start=0
    numsStart=0
    numsEnd=0

    for i in range(len(nums)):
        if sum1==0:
            start=i
        
        sum1+=nums[i]

        if sum1 > maxi:
            maxi=sum1
            numsStart=start
            numsEnd=i
        
        if sum1<0:
            sum1=0
    
    return [numsStart,numsEnd]

def main():
    nums= [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_subarray(nums))
main()
