T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    beam = 1
    wall = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                wall += 1 #벽 개수 카운트

            
            if arr[i][j] == 2:
                xi, xj = i, j

                # 상하좌우 레이저
                for d in range(4):
                    for c in range(1, N):
                        ni = xi + di[d] * c
                        nj = xj + dj[d] * c

                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 0:
                                beam += 1 #빔 카운트
                            else:
                                break

    safe = N * N - (wall + beam)
    print(f'#{tc} {safe}')