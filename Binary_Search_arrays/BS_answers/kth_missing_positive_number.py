#Time Complexity : O(N)

def find_missing_number(nums,k):
    n=len(nums)
    low = 0
    high = n - 1
    while low<=high:
        mid = (low+high)//2
        missing = nums[mid]-(mid+1)
        if missing<k:
            low = mid + 1
        else:
            high = mid - 1
    return low + k  # or high+k+1

def main():
    arr = [2,3,4,7,11]
    k = 5
    print(find_missing_number(arr,k))
main()