while q:
    i, j= q.pop(0)
    if maze[i][j]==3:
        return visited[i][j]==3:
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]
        ni, nj = i + di, j +dj
        if 0<=ni<N and 0 <=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
            q.append((ni,nj)) = visited[i][j]+1 #인큐
        #인큐 표시