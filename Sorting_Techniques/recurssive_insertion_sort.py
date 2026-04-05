def recurssive_insertion_sort(nums,i):
    if i == len(nums) :
        return
    
    j=i-1
    key=nums[i]
     
    while nums[j]> key and j >=0:
        nums[j+1]=nums[j]
        j=j-1

    nums[j+1]=key

    recurssive_insertion_sort(nums,i+1)

def main():
    nums=[5,4,3,2,1,6]
    recurssive_insertion_sort(nums,1)
    print(nums)
main()
