T = int(input())

for tc in range(1, T+1):
    # N : 정점 개수
    # M : 간선 개수
    N , M = map(int, input().split())

    # 인접 행렬 
    G = [[]for _ in range(N + 1)]

    for _ in range(M):
        s, e = map(int, input().split())

        G[s].append(e)
        G[e].append(s)

    # D[x][y] -> x정점에서 시작 했을때  y 정점까지 도착하는데 걸리는 최장 거리
    D = [[0] * (N+1) for _ in range(N + 1)]

    # s : 시작 정점 번호
    # v : 현재 정점 번호

    # path : 지금까지 거쳐온 정점 번호 리스트
    #DFS
    def DFS (s,v,path):
        
        # 현재 있는 정점 번호 v

        # v에서 갈 수 있는 다른 정점 nv를 발견 하면
        # 바로 nv로 이동
        
        #G[v] = [1,2,3,4,5]
        for nv in G[v]:
            # nv번호가 지금까지 왔던 길에 없었으면 이동 가능
            if nv not in path:
                path.append(nv)
                #이전에  nv 까지 왔었따면, 지나친 정점의 개수가 D[s][nv] 에 있다
                
                D[s][nv] = max(D[s][nv],len(path))
                DFS(nv,path)
                path.pop()

    # 모든 정점에서 DFS 탐색 시작
    for i in range(1, N+1):
        D[i][i] = 1
        # i 번 정점에서 시작, 현재 정점번호도 i, 지나친 정점 번호 i 추가한 상태로
        DFS(i,i,[i])

    #모든 경로 다 확인해보기
    for i in range(1,N+1):
        for j in range(1, N+1):
            max_D = max(max_D, D[i][j])

    print(f'#{tc} {max_D}')
    

