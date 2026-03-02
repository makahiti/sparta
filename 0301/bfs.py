from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]


    si, sj =0 ,0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2: #출발점
                si, sj = i, j

    visited=[[0]*N for _ in range(N)]
    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    def bfs(si, sj):
        queue = deque()
        queue.append((si,sj))
        visited[si][sj] = 1 

        while queue:
            i, j = queue.popleft()

            if matrix[i][j] == 3: # 도착점
                return visited[i][j] - 1 # 시작칸 제외
            
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and matrix[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))
                    
        return 0
    
    print(f'#{tc} {bfs(si, sj)}')