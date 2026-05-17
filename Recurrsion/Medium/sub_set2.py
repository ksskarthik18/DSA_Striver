def sub_set2(nums):
    result=[]
    nums.sort()
    def backTrack(index,ds):
        result.append(ds[:])
        for i in range(index,len(nums)):
            if i > index and nums[i]==nums[i-1]:
                continue
            ds.append(nums[i])
            backTrack(i+1,ds)
            ds.pop()
    backTrack(0,[])
    return result

def main():
    nums = [1,2,2]
    print(sub_set2(nums))

main()
