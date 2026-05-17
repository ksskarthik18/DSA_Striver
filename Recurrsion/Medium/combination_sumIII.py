#Time Complexity : O(2**9)

def combination_sumlll(k,n):
    result=[]
    def backTrack(start,target,ds):
        if target == 0 and len(ds) == k:
            result.append(ds[:])
            return
        if len(ds) > k:
            return
        
        for i in range(start,10):
            if i > target:
                return
            ds.append(i)
            backTrack(i+1,target-i,ds)
            ds.pop()
    backTrack(1,n,[])
    return result

def main():
    k = 3
    n = 7
    print(combination_sumlll(k,n))
main()