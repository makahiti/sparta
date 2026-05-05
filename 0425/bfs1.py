from collections import deque

T = 1

V,E = map(int,input().split())

adj_lst = [[]for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

S ,G = map(int, input().split())

visited = [0]*(V+1)

def bfs():
    q = deque()
    q.append(S)
    visited[S] = 1

    while q:
        v = q.popleft()

        if v == G:
            return visited[v] - 1

        for nv in adj_lst[v]:
            if not visited[nv]:
                visited[nv] = visited[v] + 1
                q.append(nv)

    return 0

print(bfs())