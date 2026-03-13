#탈주범 검거
#지도 = 이차원리스트

# BFS 상세
# - 탐색 : 상하좌우
# - 이동이 불가능한 케이스
# - [델타배열기본] 범위밖으로 못나감
# - [방문기록기본] 이미 방문한 곳은 못감
# - [0이면 못감]
# - 문제조건
#       -현재 내 위치에서 뚫려있는 곳만 이동 가능
#       - 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
#           -> 델타배열과 동일한 순서로 "이동 가능 여부를 기록" 하면 좋겠다

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}
def bfs(R, C):
    q = deque([R, C])
    visited[R][C] = 1

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]

        # 현재 좌표로부터 갈 수 있는 모든 노드를 확인
        # - 우리 문제에서는 상하좌우
        # - 이동이 가능한 다음 좌표만 q에 추가
        for i in range(4):
            # i 방향이 안뚫리면 못감
            if dirs[dir] == 0:
                continue
            # j 방향이 안뚫리면 못감
            if dirs[dir]
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            # - [델타배열기본] 범위밖으로 못나감
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            # - [방문기록기본] 이미 방문한 곳은 못감
            if visited[ny][nx]:
                continue
            # - [0이면 못감]
            if graph[ny][nx] == 0:
                continue

            # 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
            next_dirs = types[graph[ny][nx]]

            # 현재 상,좌 -> next_dirs 가 하,우가 안뚫리면 못감
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
            # 현재 하,우 -> next_dirs 가 상,좌가 안뚫리면 못감
            if dir % 2 == 0 and next_dirs[dir - 1] == 0:

            # 시간을 + 1 누적하면서 이동
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))
    pass

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split()))for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

