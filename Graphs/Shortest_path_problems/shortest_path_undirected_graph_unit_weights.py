# Time Complexity : O(V + E)
from collections import deque
def shortest_path_undirected_graph_unit_weights(V,edges,src):
    graph = [[] for _ in range(V)]
    distance = [-1]*V
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()

    distance[src] = 0
    queue.append(src)

    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)

    return distance
V= 9
edges = [[0,1],[0,3],[3,4],[4,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src = 0
print(shortest_path_undirected_graph_unit_weights(V,edges,src))