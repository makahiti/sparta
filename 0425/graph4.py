from collections import deque

graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2],
    [3]
]

visited = [0] * 6

def bfs(start):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for next in graph[v]:
            if visited[next] == 0:
                visited[next] = visited[v] + 1
                queue.append(next)

bfs(1)

print(visited[5])