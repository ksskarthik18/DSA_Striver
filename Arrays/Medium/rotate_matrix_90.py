def rotate_matrix_90_degree(matrix):
    n=len(matrix)
    m=len(matrix[0])

    for i in range(n-1):
        for j in range(i+1,n,1):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    return matrix

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate_matrix_90_degree(matrix))
main()