from collections import deque

T = int(input())

for tc in range(1, T+1):
    # V=노드개수, E는 간선의 개수
    V,E = map(int, input().split())
    #인접리스트 만들기
    adj_lst = [[0]for _ in range(V+1)]

    # E 개의 양쪽 노드의 개수
    for _ in range(E):
        A, B = map(int,input().split())
        adj_lst[A].append(B)
        adj_lst[B].append(A)

    # 출발노드, 도착노드 S,G
S, G = map(int, input().split())

    # visited 배열 만들기
visited = [0] * V+1

def bfs ():
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