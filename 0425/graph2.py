graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 5],
    [2],
    [3]
]

visited = [False] * 6

def dfs(v):
    visited[v]=True
    print(v, end='')

    for next in graph[v]:
        if not visited[next]:
            dfs(next)


dfs(1)