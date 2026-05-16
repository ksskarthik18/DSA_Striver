def combination_sum2(arr,target):
    arr.sort()
    result =[]
    def backTrack(i,target,ds):
        if target == 0:
            result.append(ds[:])
            return
        
        for j in range(i,len(arr)):
            if j > i and arr[j] == arr[j-1]:
                continue
            if arr[j] > target:
                break
            ds.append(arr[j])
            backTrack(j+1,target-arr[j],ds)
            ds.pop()
    backTrack(0,target,[])
    return result

def main():
    arr = [10,1,2,7,6,1,5]
    target = 8
    print(combination_sum2(arr,target))
main()
        