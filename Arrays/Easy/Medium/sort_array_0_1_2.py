def sortarray(nums):
    low=0
    mid=0
    high=len(nums)-1

    #0 - low-1 0
    #low - mid-1 1
    #mid -high random
    #high+1 - n-1 2
    while mid<= high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        
        elif nums[mid]==1:
            mid+=1

        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    
    return nums

def main():
    nums=[0,0,1,1,1,2,1,2,0,0,0]
    print(sortarray(nums))

main()

