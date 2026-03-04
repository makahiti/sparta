T = int(input())

for tc in range(1,T+1):
    N,M= map(int, input().split())
    
    arr=[list(int, input().split())for _ in range(M)]
    
    #delta
    di=[-1,1,0,0] + [-1,-1,1,1]
    dj=[0,0,-1,1] + [-1,1,1,-1]
    
    board=[[0] for _ in range(N)]
    #백돌
    board[N//2][N//2] = 2
    board[N//2][N//2-1] = 2
    #흑돌
    board[N//2-1][N//2] = 2
    board[N//2][N//2-1] = 2

    
    for _ in range(M):
        
        i,j,color = map(int,input().split())
        
        i -= 1
        j -= 1
        board[i][j]=color
        
    for d in range(8):
        
        reverse_lst=[]
        for k in range(1,N):
            ni = i + di[d]*k
            nj = j + dj[d]*k
            
            if not (0 <= ni < N and 0<= nj < N):
                break
            
            elif board[ni][nj] == 0:
                break
            
            elif board[ni][nj] != color:
                reverse_lst.append((ni)(nj))
                
            elif board[ni][nj] == color:
                while reverse_lst:
                    
                    ri, rj = reverse_lst.pop()
                    board[ri][rj] = color 
            
            break
                       
        
    # for a in range(M):
    #     for b in range(M):
    #     board[[a][b]=arr[]
                   
        
        
    # for i in range(N):
    #     for j in range(N):
    #         cnt_blackstone=0
    #         cnt_whitestone=0
    #         for k in range(N):
    #             ni = i + di[k]
    #             nj = j + dj[k]
    #             if 0 <= ni < 0 and 0 <= nj < N and arr[i][j] <N:
                    
    #                 if arr[i][j] == 1:
                        
                    
                    
        