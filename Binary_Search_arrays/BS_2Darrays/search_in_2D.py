#Time Complexity : O(log n x m)

def search_in_2D(nums,target):
    n= len(nums)
    m = len(nums[0])

    low = 0
    high = n * m -1
    while low <= high:
        mid = (low + high)//2
        row = mid//m
        col = mid % m
        if nums[row][col] == target:
            return True
        elif nums[row][col]<target:
            low = mid + 1
        else :
            high = mid - 1
    return False

def main():
    nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    target = 9
    print(search_in_2D(nums,target))

main()