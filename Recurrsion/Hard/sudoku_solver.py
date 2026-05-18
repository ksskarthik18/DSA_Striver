#Time Complexity : O(9^(n²))
def solveSudoku(board):
    solve(board)
    return board
def solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for c in range(1,10):
                    if isValid(board,i,j,str(c)):
                        board[i][j] = str(c)

                        if solve(board):
                            return True
                        else:
                            board[i][j] ="."
                
                return False
    
    return True

def isValid(board,row,col,c):
    for i in range(9):
        if board[row][i] == c:
            return False
        if board[i][col] == c:
            return False
        
        if board[3 * (row//3) + (i//3)][3 * (col//3) + (i%3)] == c:
            return False
    
    return True

def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solveSudoku(board))
main()
    