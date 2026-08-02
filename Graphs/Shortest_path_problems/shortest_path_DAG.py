
#Time Complexity :
# Building graph
# for u, v, weight in edges:
# O(M)

# DFS topological sort

# Every vertex and edge is processed once:

# O(N + M)

# Distance calculation

# Again, every vertex/edge is processed:

# O(N + M)

def shortestPath_DAG(N,M,edges):
    graph = [[] for _ in range(N)]
    for a,b,weight in edges:
        graph[a].append((b,weight))
    visited = [False]*N
    topo = []

    def dfs(node):
        visited[node] = True

        for neighbour,weight in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)

        topo.append(node)



    for i in range(N):
        if not visited[i]:
            dfs(i)

    topo.reverse()

    dist = [float('inf')]*N
    dist[0] = 0

    for node in topo:
        if dist[node] == float('inf'):
            continue
        for neighbour,weight in graph[node]:
            if dist[node] + weight < dist[neighbour]:
                dist[neighbour] = dist[node] + weight

    for i in range(N):
        if dist[i] == float('inf'):
            dist[i] = -1

    return dist

N = 4
M = 2 
edges = [[0,1,2],[0,2,1]]

print(shortestPath_DAG(N,M,edges))
