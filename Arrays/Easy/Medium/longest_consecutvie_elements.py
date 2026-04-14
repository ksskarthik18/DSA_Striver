def longest_consecutive(nums):
    n=len(nums)
    set1=set(nums)
    max_len=0
    for num in set1:
        if num-1 not in set1 :
            current=num
            length=1

            while current+1 in set1:
                current+=1
                length+=1
            
            max_len=max(max_len,length)

    return max_len

def main():
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longest_consecutive(nums))
main()
