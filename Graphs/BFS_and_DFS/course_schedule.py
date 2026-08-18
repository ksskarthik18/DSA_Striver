from collections import deque
def canFinish(numCourses,prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0]*numCourses

    for course,preq in prerequisites:
        graph[preq].append(course)
        indegree[course]+=1

    queue = deque()

    for course in range(numCourses):
        if indegree[course] == 0:
            queue.append(course)

    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for next_course in graph[course]:
            indegree[next_course] -= 1

            if indegree[next_course] == 0:
                queue.append(next_course)

    return completed == numCourses

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses,prerequisites))