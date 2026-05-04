# from collections import deque


# T = 10
# for tc in range(1, T+1):

#     N = 100

#     maze = [list(map(int,input().split()))for _ in range(N)]


#     visited = [[0] * N for _ in range(N)]


# # 델타 탐색
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# # 시작점 찾기
# ss, ee = 0,0
# for i in range(N):
#     for j in range(N):
#         if maze[i][j] == 2:
#             ss, ee = i, j

# # bfs
# def bfs (ss, ee):
#     queue = deque()
#     visited [ss][ee] = 1
#     queue.append((ss,ee))

#     # 내가 서 있는 곳
#     while queue:
#         i , j = queue.popleft()

#         # 3에 서있다면(도착했다면) 리턴 1
#         if maze[i][j] == 3:
#             return 1

#             # 델타 탐색
#         for d in range(4):
#             ni = i + dx[d]
#             nj = j + dy[d]

#             if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#                 if maze[ni][nj] != 1: 
#                     visited[ni][nj] = 1
#                     queue.append((ni, nj))

#     result = bfs()
#     print(f'{tc} {result}')

from collections import deque

# 1. 함수 정의는 코드의 가장 윗부분에 두는 것이 좋습니다.
def bfs(ss, ee, maze, N):
    # visited는 매 테스트 케이스마다 새로 만들어야 합니다.
    visited = [[0] * N for _ in range(N)]
    queue = deque()  # '==' 아님, '=' 사용
    
    visited[ss][ee] = 1
    queue.append((ss, ee)) # queue = queue.append 아님!

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        i, j = queue.popleft()

        # 도착점 확인
        if maze[i][j] == 3:
            return 1

        # 델타 탐색
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if maze[ni][nj] != 1: 
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
    
    return 0 # 도착 못하면 0 리턴

# 2. 메인 실행 루프
T = 10
for _ in range(1, T + 1):
    tc = int(input()) # 테스트 케이스 번호 입력
    N = 100
    # 3. 100줄의 미로 입력 (공백 없는 숫자의 경우)
    maze = [list(map(int, input())) for _ in range(N)]

    # 4. 시작점 찾기는 미로 입력 바로 다음에!
    ss, ee = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ss, ee = i, j
                break # 시작점 찾으면 안쪽 루프 탈출

    # 5. 함수 호출 및 결과 출력
    result = bfs(ss, ee, maze, N)
    print(f'#{tc} {result}')