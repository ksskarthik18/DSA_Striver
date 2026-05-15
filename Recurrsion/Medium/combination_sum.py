#Time Complexity :  2^T X K
def combination_sum(arr,target):
    result = []
    def backTrack(i,target,ds):
        if target == 0:
            result.append(ds[:])
            return
        if i == len(arr):
            return
        
        if arr[i]<= target:
            ds.append(arr[i])
            backTrack(i,target-arr[i],ds)
            ds.pop()
        backTrack(i+1,target,ds)
    
    backTrack(0,target,[])
    return result

def main():
    arr = [2,3,5]
    target = 8
    print(combination_sum(arr,target))
main()

