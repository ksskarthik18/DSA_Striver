def alternate_way(nums):
    n=len(nums)
    result=[0]*n
    pos=[]
    neg=[]
    for i in range(n):
        if nums[i] < 0:
            neg.append(nums[i])
        else:
            pos.append(nums[i])

    if len(pos) > len(neg):
        for i in range(len(neg)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        index=len(neg)*2

        for i in range(index,len(pos),1):
            nums[index]=pos[i]

    else:
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
            index=len(pos)*2

        for i in range(index,len(neg),1):
            nums[index]=neg[i]
    
    return nums
    
def main():
    nums=[1,2,-4,-5,6,7]
    print(alternate_way(nums))
main()

