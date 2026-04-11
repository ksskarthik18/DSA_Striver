def single_number(nums):
    result=0
    for num in nums:
        result ^=num
    return result

def main():
    nums=[4,1,2,1,2,3,3]
    print(single_number(nums))
main()