def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가 ?
    for i in range(row):
        if visited[i][col]:
            return True
    # 2. 좌상단 대각선에 놓은 적이 있는가 ?
    i, j = row -1, col -1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return True
        i -= 1
        j -= 1
    # 3. 우상단 대각선에 놓은 적이 있는가 ?
    i, j = row -1, col -1
    while i >= 0 and j < N:
        if visited[i][j]:
            return True
        i -= 1
        j += 1

# depth: 모든 행에 퀸을 놓았는가 ? (N개)
# branch: 모든 열에 퀸을 놓았는가 ? (N개)

def recur(row):
    global answer

    if row == N:
        answer += 1
        print(path)
        return

    for col in range(N):
        # 유망하지 않는 경우는 못보도록 continue / 가지치기
        # 좌상단/우상단/행에 놓은 적이 있다면:
        if check(row, col):
            continue

        visited[row][col] = 1
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[row][col] = 0


N = 5 # 판 크기
answer = 0 #가능한 정답 수
path = []
#N*N 배열의  모든 위치 확인
visited = [[0] * N for _ in range(N)]#해당 열에 퀸을 놓았는지 기록
recur(0)
print(f'경우의 수 = {answer}')