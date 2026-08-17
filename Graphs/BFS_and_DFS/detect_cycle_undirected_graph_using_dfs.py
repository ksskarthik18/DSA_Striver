def has_cycle(graph):
    n = len(graph)
    visited = [False]*n
    def dfs(node,parent):
        visited[node] = True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if dfs(neighbour,node):
                    return True
            elif neighbour != parent:
                return True
        return False
    for start in range(n):
        if not visited[start]:
            if dfs(start,-1):
                return True
    return False

graph = [
    [],          # 0
    [2, 3],      # 1
    [1, 5],      # 2
    [1, 4, 6],   # 3
    [3],         # 4
    [2, 7],      # 5
    [3, 8],      # 6
    [5],         # 7
    [6]          # 8
]
print(has_cycle(graph))