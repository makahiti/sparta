N, M = map(int, input().split())

# 2차원 배열 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = -1  # 초기값은 -1 (배열 내 값이 최소 1 이상이므로)

# 2차원 배열 탐색
for i in range(N):
    for j in range(M):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            
# 결과 출력 (최대값과 위치)
print(max_val)
