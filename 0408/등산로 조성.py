T = int(input())

for tc in range(1, T+1):
    N,K=map(int, input().split())
    
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은곳에서만 등산로를 만들 수 있다.
    # 가장 높은 곳의 높이
    max_h = 0
    # 가장 높은곳 좌표 리스트
    h_list=[]
    for i in range(N):
        for j in range(N):
            # 가장 높은 곳의 좌표
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]
                h_list = []
            # 가장 높은 곳의 좌표 발견시 리스트에 추가
            elif max_h == mountain[i][j]:
                h_list.append((i,j))
        
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    max_l = 0

    # (i,j):
    # cut : 내가 깎을 기회
    # l : 등산로의 길이
    def dfs(i,j,cut,l,path):
        global max_l
        
        # 4방향 탐색해서 갈 수 있으면 가고 못 가면 안 가
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            
        if 0 <= ni < N and 0 <= nj < N not in path:
            #(ni,nj) 가 내 현재 위치보다 높이가 낮으면 그냥 가면 된다.
            if mountain[ni][nj] < mountain[i][j]:
                path.append((ni,nj))
                dfs(ni,nj,cut,l+1)
            
            #깎을 기회가 남아있다면 깎아보고 진행
            if cut :
                #깎을 수 있는 높이는 1부터 K까지 가능
                for nh in range(mountain[i][j] - K,mountain[i][j]):
                    #깎은 높이가 내 현재 높이보다 낮아야 이동 가능
                    if nh < mountain[i][j]:
                        dfs(ni,nj,0,l+1)

# 등산로 조성 시작
for si, sj in h_list:
    # 깎기 기회 1번, 등산로 길이 1부터 시작
    dfs(si,sj,1,1,[(si,sj)])

print(f'#{tc} {max_l}')

                    