def set_matrix_zeros(matrix):
    col0=1
    n=len(matrix)
    m=len(matrix[0])

    for i in range(n):
        if matrix[i][0] == 0:
                col0=0
        for j in range(1,m):
            if matrix[i][j] == 0:
                matrix[i][0]=0
                matrix[0][j]=0
    
    for i in range(1,n,1):
        for j in range(1,m,1):
            if matrix[i][j]!=0:
                if matrix[0][j] == 0 or matrix[i][0]==0:
                    matrix[i][j]=0

    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    
    if col0==0:
        for i in range(n):
            matrix[i][0]=0
    
    return matrix

def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(set_matrix_zeros(matrix))
main()


