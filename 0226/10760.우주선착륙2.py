T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, -1, 0, 0, 1, 1, -1, -1] #초강력델타검색
    dj = [0, 0, 1, -1, 1, -1, 1, -1] 

    result=0
    for i in range(N):
        for j in range(M):
 
            cnt = 0
            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < M: 
                    if arr[ni][nj] < arr[i][j]:
                        cnt += 1
            if cnt >= 4:
                result += 1

    print(f'#{tc} {result}')




 


 