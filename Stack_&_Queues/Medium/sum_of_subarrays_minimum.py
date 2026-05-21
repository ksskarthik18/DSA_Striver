def sum_subarray(nums):
    MOD =10**9+7
    n = len(nums)
    stack = []

    #Previous smaller
    pse = findPSE(nums,n)
    nse = findNSE(nums,n)
    total = 0
    for i in range(n):
        left = i - pse[i]
        right = nse[i] - i
        total += (left*right*nums[i])%MOD
        total = total%MOD
    return total
def findPSE(nums,n):
    stack =[]
    pse = [-1]*n
    for i in range(n):
        while len(stack)!=0 and nums[stack[-1]] > nums[i]:
            stack.pop()
        if len(stack) == 0:
            pse[i] = -1
        else:
            pse[i] = stack[-1]
        stack.append(i)
    return pse

def findNSE(nums,n):
    stack = []
    nse = [-1]*n

    for i in range(n-1,-1,-1):
        while len(stack)!=0 and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if len(stack) == 0:
            nse[i] = n
        else:
            nse[i] = stack[-1]
        stack.append(i)
    return nse        
    
def main():
    nums = [3,1,2,4]
    print(sum_subarray(nums))
main()