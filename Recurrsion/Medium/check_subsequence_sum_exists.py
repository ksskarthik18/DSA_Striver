#Time Complexity : O(n)
def check_subsequence(arr,target):
    def backTrack(i,s):
        if s == target:
            return True
        if i == len(arr):
            return False
        
        left = backTrack(i+1,s+arr[i])
        right = backTrack(i+1,s)

        return left + right
    return backTrack(0,0)

def main():
    arr = [1, 2, 3, 4, 5]
    target = 8
    if check_subsequence(arr,target):
        print("Yes")
    else:
        print("No")
main()