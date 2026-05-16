
def sub_set_sum(nums):
    result = []
    def backTrack(index,current):
        if index == len(nums):
            result.append(current)
            return
        
        backTrack(index+1,current+nums[index])
        backTrack(index+1,current)
    backTrack(0,0)
    return result

def main():
    nums = [2,3]
    print(sorted(sub_set_sum(nums)))
main()