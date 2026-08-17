#Time Complexity : O(V + E)
from collections import deque
def has_cycle(graph):
    n = len(graph)
    visited = [False]*n
    for start in range(n):
        if visited[start]:
            continue
        queue = deque()
        queue.append((start,-1))
        visited[start] = True

        while queue:
            node,parent = queue.popleft()

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append((neighbour,node))
                elif neighbour != parent:
                    return True
    return False

graph = [
    [],          # 0
    [2, 3],      # 1
    [1, 5],      # 2
    [1, 4, 6],   # 3
    [3],         # 4
    [2, 7],      # 5
    [3, 7],      # 6
    [5,6],         # 7
]
print(has_cycle(graph))
        