from collections import deque

T = int(input())

for tc in range(N):
    N,W,H=map(int, input().split())
    arr=[list(map(int,input().split()))for _ in range(H)]
    min_answer = 1e9

    blocks = 0 


    #구슬이 벽돌에 닿는다
    #벽돌은 터지면서 상하좌우로 숫자만큼 제거
    #가장자리 처리 
    
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    def recur(cnt, remain_blocks, now_arr):
        global min_answer

        3
        
        if cnt == N or remain_blocks == 0:
            min_answer = min(min_answer, remain_blocks)
            return
        
        for col in range(W):
            copy_arr = [row[:] for row in now_arr]

            row = -1
            for r in range(H):
                if copy_arr[r][col]:
                    row = r
                    break

            if row == -1:
                continue
            











    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1