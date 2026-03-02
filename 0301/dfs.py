T=int(input())

for tc in range(1,T+1):
    N=int(input())
    matrix=[list(map(int, input()))for _ in range(N)]
    
    si, sj = 0,0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2: #출발점 지정
                si, sj = i, j

    visited = [[0]*N for _ in range(N)]      # visited 배열 새애성    
    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    def dfs(si,sj):
        visited[si][sj] = 1 #방문처리
        stack = []

        i, j = si, sj
        while True:
            if matrix[i][j] == 3: #도착점 
                return 1
            
            for d in range(4):
                ni = i +di[d]
                nj = j +dj[d]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and matrix[ni][nj] != 1:
                    visited[ni][nj] = 1
                    stack.append((i,j))
                    i, j = ni, nj
                    break

            else:
                if stack:
                    i, j = stack.pop()

                else:
                    break
        
        return 0
    
    print(f'#{tc} {dfs(si,sj)}')
                