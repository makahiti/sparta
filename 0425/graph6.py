graph = [
    [],
    [2],        # 1
    [1, 3],     # 2
    [2],        # 3
    [5],        # 4
    [4],        # 5
    []          # 6
]

visited = [0] * 7
count = 0

def dfs(v):
    visited[v]=True

    for next in graph[v]:
        if not visited[next]:
            dfs(next)

for i in range(1, 7):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)