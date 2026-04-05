def quick_sort(nums,low,high):
    if low<high :
        pi = partition(nums,low,high)
        quick_sort(nums,low,pi-1)
        quick_sort(nums,pi+1,high)

def partition(nums,low,high):
    pivot =nums[low]
    i = low
    j = high

    while i < j :

        while i <= high -1 and nums[i] <= pivot:
            i+=1
        
        while j >=low + 1 and nums[j] > pivot :
            j-=1

        if i < j :
            nums[i],nums[j] = nums[j],nums[i]
    
    nums[low],nums[j]=nums[j],nums[low]

    return j

def main():
    nums=[5,4,3,2,1,6]
    quick_sort(nums,0,len(nums)-1)
    print(nums)
main()

    
