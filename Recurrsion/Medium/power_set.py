def generate_power_set(nums):
    result=[]
    def backTrack(index,current):
        if index == len(nums):
            result.append(current[:])
            return
        
        current.append(nums[index])
        backTrack(index+1,current)

        current.pop()

        backTrack(index+1,current)

    backTrack(0,[])

    return result

def main():
    nums = [1, 2, 3]
    print(generate_power_set(nums))
main()
