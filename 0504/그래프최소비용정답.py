from heapq import heappush, heappop
  
T = int(input())
  
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
  
  
def dijkstra():
    q = []
    heappush(q, (0, 0, 0))  # 좌측 상단 시작
    fuel[0][0] = 0
  
    while q:
        w, r, c = heappop(q)
        # r,c 까지의 사용량 w
  
        # 방금 꺼내온 r,c 까지의 사용량 w가
        # 이전에 계산해 놓은 r,c 까지의 사용량 보다 크면 계산 x
        if fuel[r][c] < w:
            continue
  
        # r,c와 연결된 노드들 탐색 => 4방향탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                # nr,nc가 갈수 있는 노드
                # nr,nc 가 r,c보다 높이가 높은지 계산
                height_diff = 0
                if arr[nr][nc] > arr[r][c]:
                    height_diff = arr[nr][nc] - arr[r][c]
  
                # nr, nc 까지 이동하는데 사용한 연료량 = r,c까지 이동하는데 사용한 연료량 + 기본 사용 + 높이 차
                # 이전에 계산해놓은 nr,nc까지 이동하는데 사용한 연료량보다 작으면 갱신
                cost = fuel[r][c] + height_diff + 1
                if cost < fuel[nr][nc]:
                    fuel[nr][nc] = cost
                    # 갱신이 일어나면 추가
                    heappush(q, (cost, nr, nc))
  
INF = 100000001
  
for tc in range(1, T + 1):
    N = int(input())
  
    arr = [list(map(int, input().split())) for _ in range(N)]
    fuel = [[INF] * N for _ in range(N)]
    fuel[0][0] = 0
    dijkstra()
  
    print(f"#{tc} {fuel[N - 1][N - 1]}")
  
"""
  
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
"""