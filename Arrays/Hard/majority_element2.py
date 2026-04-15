def majority_element2(nums):
    count1=count2=0
    element1=element2=None
    n=len(nums)

    for i in range(n):
        if count1==0 and nums[i]!=element2:
            element1=nums[i]
            count1+=1
        
        elif count2==0 and nums[i]!=element1:
            element2=nums[i]
            count2+=1

        elif nums[i]==element1:
            count1+=1
        elif nums[i]==element2:
            count2+=1
        else:
            count1-=1
            count2-=1
    
    cnt1=0
    cnt2=0
    result=[]
    for i in range(n):
        if element1==nums[i]:
            cnt1+=1
        if element2==nums[i]:
            cnt2+=1

    mini= (n//3)+1
    if cnt1>=mini :
        result.append(element1)
    if cnt2>=mini:
        result.append(element2)
    result.sort()
    return result

def main():
    #nums = [3,2,3]
    nums = [1,2]

    print(majority_element2(nums))
main()

