from collections import deque

maze = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

N = 3
M = 3

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

bfs(0, 0)

print(maze[N-1][M-1])
