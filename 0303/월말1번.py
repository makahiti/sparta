T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, 1 + T):
    N = int(input())  # 행렬 크기 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]  #행렬생성

    cnt_safty = 0  # 안전 구역 개수 카운트 변수

    # 우, 좌, 상, 하 방향 델타
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

   
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:  # 술래(2)의 위치를 찾기
                
                for d in range(4):
                    for step in range(1, N):
                        ni = i + di[d] * step
                        nj = j + dj[d] * step

                        # 범위 안에 있을 때만 확인
                        if 0 <= ni < N and 0 <= nj < N:
                            # 벽을 만나면 해당 방향 탐색 중단
                            if matrix[ni][nj] == 1:
                                break
                            # 빈 공간은 감시 구역으로 변경
                            elif matrix[ni][nj] == 0:
                                matrix[ni][nj] = 3
                        else:
                            # 범위를 벗어나면 중단
                            break

    # 감시되지 않은 안전 구역 개수 세기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                cnt_safty += 1

    # 결과 출력
    print(f'#{tc} {cnt_safty}')