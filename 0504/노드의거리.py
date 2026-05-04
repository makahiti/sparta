from collections import deque

T = int(input())

for tc in range(1, T+1):

    V, E = map(int,input().split())
    # 인접 리스트 생성    
    adj_lst = [[]for _ in range(V+1)]

    # E 개의 간선 정보를 인접리스트에 저장(무향)
    for _ in range(E):
        u, v = map(int,input().split())
        adj_lst[u].append(v)
        adj_lst[v].append(u)

    # 출발 노드 S와 도착 노드 G 입력
    S, G = map(int,input().split())

    def bfs(S,G,adj_lst,V):
        # visited 배열을 거리 기록용으로 사용
        visitied = [0] * (V + 1)
        queue = deque([S])
        visitied[S] = 1 #시작점 방문 표시 (거리는 1부터 시작한다고 가정)

        while queue :
            curr = queue.popleft()

            #현재 노드가 도착점(G) 이면 거리 반환
            if curr == G:
                # 시작할 때 1을 더했으므로, 간선 개수를 구하려면 1을 뺀다
                return visitied[curr] - 1
            
            for next_node in adj_lst[curr]:
                if not visitied[next_node]: #아직 방문 하지 않았따면
                    # 이전 노드 거리 + 1을 해서 저장
                    visitied[next_node] = visitied[curr] + 1
                    queue.append(next_node)
            # 큐가 빌 때까지 G를 못 찾았다면 연결되지 않은 것임
        return 0

    result = bfs(S, G, adj_lst, V)
    print(f'#{tc} {result}')
