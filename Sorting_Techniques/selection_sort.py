def selection_sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        
        nums[i],nums[minpos]=nums[minpos],nums[i]
    return nums
nums=[5,4,3,2,1]
print(selection_sort(nums))