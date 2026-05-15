def count_all_subsequences_sum_k(arr,target):
    def backTrack(i,s):
        if i == len(arr):
            if s == target:
                return 1
            return 0
        
        left = backTrack(i+1,s+arr[i])
        right = backTrack(i+1,s)

        return left + right
    return backTrack(0,0)

def main():
    nums=[1,10,4,5]
    target=20
    print(count_all_subsequences_sum_k(nums,target))
main()  
