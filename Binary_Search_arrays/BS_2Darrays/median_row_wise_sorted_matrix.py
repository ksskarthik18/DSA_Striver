def upper_bound(matrix,x,m):
    low = 0
    high = m -1
    ans = m
    while low<= high:
        mid = (low + high)//2
        if matrix[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def find_median(matrix):
    n = len(matrix)
    m = len(matrix[0])
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    req = (n*m)//2
    while low<= high:
        mid = (low +high)//2
        smaller = black_box(matrix,n,m,mid)
        if smaller <= req:
            low = mid + 1
        else :
            high = mid - 1
    return low

def black_box(matrix,n,m,mid):
    cnt=0
    for i in range(n):
        cnt += upper_bound(matrix[i],mid,m)
    return cnt

def main():
    matrix = [[1,5,7,9,11],[2,3,4,8,9],[4,11,14,19,20],[6,10,22,99,100],[7,15,17,24,28]]
    print(find_median(matrix))
main() 