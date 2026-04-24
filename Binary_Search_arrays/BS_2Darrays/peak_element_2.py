#Time Complexity : O (log m x n)

def find_peak_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = m - 1
    while low<=high:
        mid = (low + high)//2
        row = maxElement(matrix,n,m,mid)
        left = matrix[row][mid-1] if mid -1 >= 0 else -1
        right = matrix[row][mid+1] if mid +1 <m else -1

        if matrix[row][mid]>left and matrix[row][mid]>right:
            return [row,mid]
        elif matrix[row][mid]<left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1,-1]

def maxElement(matrix,n,m,col):
    maxVal = -1
    index = -1
    for i in range(n):
        if matrix[i][col]> maxVal:
            maxVal = matrix[i][col]
            index = i
    return index

def main():
    matrix = [[10,20,15],[21,30,14],[7,16,32]]

    print(find_peak_matrix(matrix))
main()




