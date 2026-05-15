def find_subsequence(arr,target):
    result=[]
    def backTrack(i,ds,s):
        if i == len(arr):
            if s == target:
                result.append(ds[:])
            return
        
        ds.append(arr[i])
        backTrack(i+1,ds,s+arr[i])

        ds.pop()
        backTrack(i+1,ds,s)
    backTrack(0,[],0)

    return result

def main():
    arr=[4,9,2,5,1]
    target=10
    print(find_subsequence(arr,target))
main()