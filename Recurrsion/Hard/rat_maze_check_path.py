def check_path(grid,n):
    visited =[[False]*n for _ in range(n)]

    def backTrack(r,c):
        if r == n-1 and c == n-1:
            return True
        
        visited[r][c] = True
        directions =[(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in directions:
            nr = r + dr
            nc = c + dc

            if (0<= nr < n and 0 <= nc <n and grid[nr][nc] == 1 and not visited[nr][nc]):
                if backTrack(nr,nc):
                    return True
        
        return False
    
    return backTrack(0,0)

def main():
    grid = [
        [1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]
    ]
    n = 4
    print(check_path(grid,n))
main()     
