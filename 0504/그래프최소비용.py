from heapq import heappush, heappop

T = int(input())

dr = [0,0,-1,1]
dc = [-1,1,0,0]

for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int,(input())))for _ in range(N)]
    inf = 10000000
    fuel = [[inf] * N for _ in range(N)]



    def dijkstra():
        q = []
        heappush(q, (0,0,0)) # 좌측 상단 시작
        fuel[0][0] = 0

        while q:
            w, r, c = heappop(q)
            # r,c 까지의 사용량 w

            if fuel[r][c] < w:
                continue

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0<= nc < N:
                    height_diff = 0
                    if H[nr][nc] > H[r][c]:
                        height_diff = H[nr][nc] - H[r][c]

                    cost = fuel[r][c] + height_diff + 1
                    if cost < fuel[nr][nc]:
                        fuel[nr][nc] = cost
                        heappush(q, (cost, nr, nc))


    dijkstra()
    print(f'#{tc} {fuel[N - 1][N - 1]}')


