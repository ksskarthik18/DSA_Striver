def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    
    return nums

nums=[5,4,3,2,1,6]
print(bubble_sort(nums))