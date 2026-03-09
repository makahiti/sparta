
T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):

    N, M = map(int, input().split())  # N행 M열

    flag = [input() for _ in range(N)]  # 깃발 입력

    ans = 2500  # 최대 N*M = 2500 이므로 충분히 큰 값

    # W구간 끝나는 행 i
    for i in range(N-2):

        # B구간 끝나는 행 j
        for j in range(i+1, N-1):

            repaint = 0  # 다시 칠해야 하는 칸 수

            # -------- W 구간 --------
            for r in range(0, i+1):  # 0 ~ i
                for c in range(M):
                    if flag[r][c] != 'W':  # W가 아니면 다시 칠해야함
                        repaint += 1

            # -------- B 구간 --------
            for r in range(i+1, j+1):  # i+1 ~ j
                for c in range(M):
                    if flag[r][c] != 'B':
                        repaint += 1

            # -------- R 구간 --------
            for r in range(j+1, N):  # j+1 ~ N-1
                for c in range(M):
                    if flag[r][c] != 'R':
                        repaint += 1

            # 최소값 갱신
            ans = min(ans, repaint)

    print(f"#{tc} {ans}")