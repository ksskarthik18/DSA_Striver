def recurssive_bubble_sort(nums,n):
    if n==1:
        return
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
    
    recurssive_bubble_sort(nums,n-1)

def main():
    nums=[5,4,3,2,1,6]
    recurssive_bubble_sort(nums,len(nums))
    print(nums)
main()