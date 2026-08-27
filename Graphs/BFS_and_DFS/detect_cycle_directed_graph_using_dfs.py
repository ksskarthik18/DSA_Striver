#Time Complexity : O(V + E)
def has_cycle(V,edges):
    visited = [False]*V
    path_visited = [False]*V

    def dfs(node):
        visited[node] = True
        path_visited[node] = True

        for neighbour in edges[node]:
            if not visited[neighbour]:
                if dfs(neighbour):
                    return True
            elif path_visited[neighbour]:
                return True

        path_visited[node] = False
        return False
    for start in range(V):
        if not visited[start]:
            if dfs(start):
                return True

    return False
# V = 4
# adj= [[1,2], [2], [], [0,2]]
V = 6
adj= [ [1], [2, 5], [3], [4], [1], [ ] ]

print(has_cycle(V,adj))