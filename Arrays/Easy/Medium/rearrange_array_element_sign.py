def rearrange_array(nums):
    posIndex=0
    negIndex=1
    n=len(nums)
    result=[0]*n
    for i in range(n):
        if nums[i]<0:
            result[negIndex]=nums[i]
            negIndex+=2

        else :
            result[posIndex]=nums[i]
            posIndex+=2
    
    return result

def main():
    nums=[3,1,-2,-5,2,-4]
    print(rearrange_array(nums))

main()


