grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

N = 4
M = 4
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    grid[x][y] = 0   # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 밖이면 무시
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        # 땅이면 계속 탐색
        if grid[nx][ny] == 1:
            dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            dfs(i, j)
            count += 1

print(count)