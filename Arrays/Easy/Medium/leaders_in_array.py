def leader_in_array(nums):
    maxi=float('-inf')
    n=len(nums)
    result=[]
    for i in range(n-1,-1,-1):
        if nums[i]>maxi:
            result.append(nums[i])
        maxi=max(maxi,nums[i])

    result.sort()
    return result

def main():
    nums=[10,22,12,3,0,6]
    print(leader_in_array(nums))
main()


