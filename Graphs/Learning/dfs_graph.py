def dfs(graph,node,visited):
    visited.add(node)
    print(node,end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
visited = set()
dfs(graph,0,visited)