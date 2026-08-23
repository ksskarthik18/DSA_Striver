#Time Complexity : O( m x n)
from collections import deque
def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    count = 0
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                grid[r][c] = '0'
                queue.append((r,c))


                while queue:
                    r,c = queue.popleft()
                    for dr,dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr,nc))

    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))
