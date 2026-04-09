from collections import deque

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    
    T = int(input_data[idx]); idx += 1
    
    # 방향을 숫자로 관리: 0=위, 1=오른쪽, 2=아래, 3=왼쪽
    # 전진 시 각 방향에 따른 행/열 변화량
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    for t in range(1, T + 1):
        N, K = int(input_data[idx]), int(input_data[idx+1]); idx += 2
        
        field = []
        start = end = None
        
        for r in range(N):
            row = input_data[idx]; idx += 1
            field.append(list(row))
            for c in range(N):
                if field[r][c] == 'X':
                    start = (r, c)   # RC카 출발 위치
                elif field[r][c] == 'Y':
                    end = (r, c)     # RC카 목적지 위치
        
        # ── BFS 설계 ──────────────────────────────────────────────────────────
        # 단순히 (행, 열)만으로는 상태가 부족하다.
        # 같은 칸에 도착해도 바라보는 방향이 다르면 이후 조작 비용이 달라지기 때문.
        # 또한 나무를 몇 개 벴는지도 상태에 포함해야,
        # "더 많은 나무를 베고 도착한 경로"와 "적게 베고 도착한 경로"를 구분할 수 있다.
        #
        # 상태: (행, 열, 방향, 지금까지_벤_나무_수)
        # 비용: 조작 횟수 (전진 / 좌회전 / 우회전 모두 1회)
        #        나무를 베는 것은 별도 조작이 아니라 전진에 포함됨
        #
        # 모든 조작의 비용이 동일(=1)하므로 다익스트라 없이 일반 BFS로 최솟값 보장.
        # ──────────────────────────────────────────────────────────────────────
        
        INF = float('inf')
        # dist[r][c][d][k] = (r,c)에서 방향 d로, 나무 k그루 벤 상태로 도달하는 최소 조작 횟수
        dist = [[[[INF] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
        
        sr, sc = start
        dist[sr][sc][0][0] = 0          # 출발: 위(0) 방향, 벤 나무 0그루, 조작 0회
        queue = deque()
        queue.append((sr, sc, 0, 0, 0)) # (행, 열, 방향, 벤_나무_수, 조작_횟수)
        
        ans = INF
        
        while queue:
            r, c, d, k, ops = queue.popleft()
            
            # 이미 더 적은 조작으로 이 상태에 도달한 적이 있으면 스킵 (중복 처리 방지)
            if ops > dist[r][c][d][k]:
                continue
            
            # 목적지 도달 시 정답 갱신
            if (r, c) == end:
                ans = min(ans, ops)
                continue
            
            # ── 조작 1: 전진 ──────────────────────────────────────────────────
            nr, nc = r + dr[d], c + dc[d]   # 현재 방향으로 한 칸 앞 좌표
            if 0 <= nr < N and 0 <= nc < N:  # 필드 범위 안에 있을 때만
                if field[nr][nc] == 'T':
                    # 앞이 나무 → 벌목 횟수가 남아 있으면 베고 전진 (조작 1회 소모)
                    if k < K:
                        new_ops = ops + 1
                        if new_ops < dist[nr][nc][d][k + 1]:
                            dist[nr][nc][d][k + 1] = new_ops
                            queue.append((nr, nc, d, k + 1, new_ops))
                else:
                    # 앞이 빈 칸(G, X, Y) → 그냥 전진 (조작 1회 소모)
                    new_ops = ops + 1
                    if new_ops < dist[nr][nc][d][k]:
                        dist[nr][nc][d][k] = new_ops
                        queue.append((nr, nc, d, k, new_ops))
            
            # ── 조작 2: 좌회전 (반시계 방향, 제자리) ─────────────────────────
            # 0(위) → 3(왼) → 2(아래) → 1(오른) → 0(위) ...
            nd = (d - 1) % 4
            if ops + 1 < dist[r][c][nd][k]:
                dist[r][c][nd][k] = ops + 1
                queue.append((r, c, nd, k, ops + 1))
            
            # ── 조작 3: 우회전 (시계 방향, 제자리) ───────────────────────────
            # 0(위) → 1(오른) → 2(아래) → 3(왼) → 0(위) ...
            nd = (d + 1) % 4
            if ops + 1 < dist[r][c][nd][k]:
                dist[r][c][nd][k] = ops + 1
                queue.append((r, c, nd, k, ops + 1))
        
        print(f"#{t} {ans if ans != INF else -1}")

solve()