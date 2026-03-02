from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    # 출발점 찾기
    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                si, sj = i, j

    visited = [[0] * N for _ in range(N)]

    # 상, 하, 좌, 우
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    def bfs(si, sj):
        queue = deque()
        queue.append((si, sj))
        visited[si][sj] = 1  # 방문 처리

        while queue:
            i, j = queue.popleft()

            # 도착점에 도달하면 통과 가능
            if matrix[i][j] == 3:
                return 1

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                # 범위 안 + 미방문 + 벽 아님
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and matrix[ni][nj] != 1:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))

        return 0  # 도착 못함 → 통과 불가

    print(f'#{tc} {bfs(si, sj)}')