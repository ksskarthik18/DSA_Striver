def max_consecutive_ones(nums):
    max1=0
    count=0
    n=len(nums)
    for i in range(n):
        if nums[i]==1:
            count+=1
            max1 = max(count,max1)
        else:
            count=0

    return max1

def main():
    nums=[1,0,1,1,1,0,0,1,1]
    print(max_consecutive_ones(nums))
main()
