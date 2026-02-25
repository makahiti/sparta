T=int(input())

for tc in range(1, T+1):
    N=int(input())
    arr=[list(input())for _ in range(N)]

    ans='NO'
    # 델타 탐색
    di = [1,0,1,1]
    dj = [0,1,1,-1]

    for i in range(N):
        for j in range(N):
            if arr[i][j]=='o': # o가 있다면
                for k in range(4):
                    cnt = 1 # 카운팅 +1
                    ni, nj = i, j
                    for _ in range(4):
                        ni += di[k]
                        nj += dj[k]

                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt == 5: #o 카운팅이 5개 (오목) 이면 YES 출력
                        ans = 'YES'
                        
    print(f'#{tc} {ans}')