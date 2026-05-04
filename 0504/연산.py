from collections import deque

T = int(input())

for tc in range(1, T+1):
    N , M = map(int,input().split())

    Max = 1000000


    def bfs(N,M):
        visited = [False] * (Max + 1)
        queue = deque()

        queue.append((N,0))
        visited[N] = True

        while queue:
            current, count = queue.popleft()

            if current == M :
                return count
            
            for next_val in (current +1,current - 1, current * 2, current -10):
                if 1 <= next_val <= Max and not visited[next_val]:
                    visited[next_val] = True
                    queue.append((next_val, count + 1))



    result = bfs(N, M)
    print (f'#{tc} {result}')



