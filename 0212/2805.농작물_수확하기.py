T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # farm의 크기
    farm = [list(map(int, input())) for _ in range(N)]  # N x N 크기의 farm

    sum_value = 0

    # 다이아몬드 영역 합 계산
    for i in range(N):
        # i가 0에서 N//2-1까지인 경우, 위쪽 삼각형 (중앙을 포함하지 않음)
        if i <= N // 2: # i가 N//2 
            # 중앙부터 좌우 대칭 영역
            for j in range(N // 2 - i, N // 2 + i + 1):
                sum_value += farm[i][j]
        else:
            # i가 N//2+1부터 N-1까지인 경우, 아래쪽 삼각형 (중앙을 포함)
            for j in range(i - N // 2, N - (i - N // 2)):
                sum_value += farm[i][j]

    print(f'#{tc} {sum_value}')
