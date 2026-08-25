#Time Complexity : O(V + E)

from collections import deque
def count_components(V,edges):
    graph = [[] for _ in range(V)]
    visited =[False]*V

    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    count = 0
    for start in range(V):
        if visited[start]:
            continue
        count += 1
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    queue.append(neighbour)

    return count
V = 7
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
print(count_components(V,edges))