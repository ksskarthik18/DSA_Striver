from collections import deque

def rottenOranges(grid):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh +=1

    minutes = 0
    while queue and fresh > 0:

        for _ in range(len(queue)):
            r,c = queue.popleft()

            directions = [
                (1,0),(-1,0),(0,1),(0,-1)
            ]
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr <rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1
                        queue.append((nr,nc))
        minutes += 1

    if fresh > 0:
        return -1
    return minutes
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rottenOranges(grid))
                    