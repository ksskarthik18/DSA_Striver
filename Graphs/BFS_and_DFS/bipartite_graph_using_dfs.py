#Time Complexity : O(V + E)
def isBipartite(graph):
    n = len(graph)
    color = [-1]*n

    def dfs(node):
        for neighbour in graph[node]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[node]

                if not dfs(neighbour):
                    return False

            elif color[neighbour] == color[node]:
                return False
        return True

    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            if not dfs(start):
                return False

    return True
graph = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartite(graph))