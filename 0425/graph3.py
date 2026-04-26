from collections import deque

graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2],
    [3]
]

visited = [False] * 6

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end = '')

        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

bfs(1)