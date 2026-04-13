def majority_element(nums):
    element=None
    count=0
    for i in range(len(nums)):
        if count==0:
            element=nums[i]
            count+=1
        
        elif nums[i] == element:
            count+=1
        else :
            count-=1
    
    count1=0
    for i in range(len(nums)):
        if nums[i]==element:
            count1+=1
    
    if count1 > len(nums)/2:
        return element
    return -1

    
def main():
    nums=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
    print(majority_element(nums))

main()


