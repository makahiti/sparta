graph = [
    [],
    [2, 5],
    [1, 3, 5],
    [2],
    [7],
    [1, 2, 6],
    [5],
    [4]
]

visited = [False] * 8
count = 0   # 감염된 컴퓨터 수

def dfs(v):
    global count
    
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            count += 1      # 새로 감염됨
            dfs(next)

dfs(1)

print(count)