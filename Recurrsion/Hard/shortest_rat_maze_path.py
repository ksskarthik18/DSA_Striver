def find_shortest_path(grid, n):

    if grid[0][0] == 0:
        return -1

    visited = [[False]*n for _ in range(n)]
    shortest =[""]

    def backTrack(r, c, path):
        if r == n-1 and c == n-1:
            if shortest[0] == "" or len(path)< len(shortest[0]):
                shortest[0] = path
            return 

        visited[r][c] = True

        # Down
        if (r+1 < n and
            grid[r+1][c] == 1 and
            not visited[r+1][c]):

            backTrack(r+1, c, path+"D")

        # Left
        if (c-1 >= 0 and
            grid[r][c-1] == 1 and
            not visited[r][c-1]):

            backTrack(r, c-1, path+"L")

        # Right
        if (c+1 < n and
            grid[r][c+1] == 1 and
            not visited[r][c+1]):

            backTrack(r, c+1, path+"R")

        # Up
        if (r-1 >= 0 and
            grid[r-1][c] == 1 and
            not visited[r-1][c]):

            backTrack(r-1, c, path+"U")

        visited[r][c] = False


    backTrack(0,0,"")

    return shortest[0] if shortest[0] else -1


def main():

    grid = [
        [1,1,1,1],
        [1,1,0,1],
        [1,1,0,1],
        [0,1,1,1]
    ]

    n = 4

    print(find_shortest_path(grid,n))

main()