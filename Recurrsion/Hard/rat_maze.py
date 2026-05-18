def find_paths(grid,n):
    visited =[[False]*n for _ in range(n)]
    if grid[0][0] == 0:
        return []
    result =[]
    def backTrack(r,c,path):
        if r == n-1 and c == n-1:
            result.append(path)
            return
        
        visited[r][c] = True
        #Down
        if r+1 < n and grid[r+1][c] == 1 and not visited[r+1][c]:
            backTrack(r+1,c,path+"D")
        #Left
        if c-1>=0 and grid[r][c-1] == 1 and not visited[r][c-1]:
            backTrack(r,c-1,path+"L")
        
        #right
        if c+1<n and grid[r][c+1] == 1 and not visited[r][c+1]:
            backTrack(r,c+1,path+"R")
        
        #Up
        if r-1<n and grid[r-1][c] == 1 and not visited[r-1][c]:
            backTrack(r-1,c,path+"U")
        
        visited[r][c] = False

    backTrack(0,0,"")
    return result

def main():
    grid = [
        [1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]
    ]
    n = 4
    print(find_paths(grid,n))
main()