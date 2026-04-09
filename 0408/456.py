import sys
sys.stdin = open("inut2.txt", "r")

from heapq import heappop, heappush

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dikjstra():
    #누적거리 , y, x
    pq = [(0, 0, 0)]
    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = 0
    pass

    while pq:
        dist, y, x = heappop(pq)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

        # 범위 밖이면 continue
        if ny < 0 or ny >= N or nx < 0 or nx <= N:
            continue

        #누적거리 계산
        # - 누적거리가 기존보다 크거나 같으면 continue
        new_dist = dist + graph[ny][nx]

        if dist[ny][nx] <= new_dist:
            continue

        dists[ny][nx] = new_dist
        heappush(pq, (new_dist, ny, nx))

    for row in dists:
        print(row)

        return dists[N-1][N-1]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split()))for _ in range(N)]

    result = dikjstra()