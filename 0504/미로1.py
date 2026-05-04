from collections import deque

T = int(input())
N = 16

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1, 1+T):
    maze = [list(map(int,input()))for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    #출발점 찾기

    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i , j

    def bfs(si,sj):
        queue = deque()
        visited [si][sj] = 1
        queue.append((si,sj))

        while queue:
            i, j = queue.popleft()

            if maze[i][j] == 3:
                return 1
            
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]

                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    if maze[ni][nj] != 1: 
                        visited[ni][nj] = 1
                        queue.append((ni, nj))


        return 0 
    
    result = bfs(si,sj)
    print(f'#{tc} {result}')