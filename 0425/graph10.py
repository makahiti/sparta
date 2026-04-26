from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))

    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 벽이면 못 감
            if maze[nx][ny] == 1:
                continue

            # 아직 방문 안 했으면
            if visited[nx][ny] == 0:

                # 도착점 발견
                if maze[nx][ny] == 3:
                    return visited[x][y] - 1

                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    result = bfs(start_x, start_y)

    print(f"#{tc} {result}")