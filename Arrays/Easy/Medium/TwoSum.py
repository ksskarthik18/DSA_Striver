def find_sum(nums,target):
    hash_map={}
    for i in range(len(nums)):
        s=target-nums[i]

        if s in hash_map:
            return [hash_map[s],i]

        hash_map[nums[i]]=i
    return []

    
def main():
    nums=[2,6,5,8,11]
    target=14
    print(find_sum(nums,target))

main()