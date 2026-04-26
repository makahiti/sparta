N=int(input())
grid=[list(map(int, input().split()))for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0

def dfs(x,y):
    grid[x][y] = 0 # 방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        #범위 밖이면 무시
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        # 땅이면 계속 탐색
        if grid[nx][ny] == 1:
            dfs(nx,ny)


for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            dfs(i, j)
            count += 1

print(count)

