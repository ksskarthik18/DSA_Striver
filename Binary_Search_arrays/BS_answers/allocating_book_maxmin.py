#Time Complexity : O(log n) x O(N)
def find_pos(nums,pages,students):
    n = len(nums)
    std_cnt=1
    t_pages=0
    for i in range(n):
        t_pages+=nums[i]
        if t_pages > pages :
            std_cnt+=1
            t_pages = nums[i]

    if std_cnt > students:
        return True
    return False


def allocate_books(nums,students):
    n = len(nums)
    low = min(nums) # it can be max(nums) also
    high = sum(nums)
    while low <= high:
        mid = (low + high)//2

        if (find_pos(nums,mid,students) == True):

            low = mid + 1
        else :
            high = mid - 1
    return low

def main():
    nums = [12,34,67,90]
    students=2
    print(allocate_books(nums,students))

main()

