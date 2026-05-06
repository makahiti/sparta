import heapq

T = int(input())

for tc in range(1, T+1):
    N,E = map(int,input().split())

    #인접리스트
    adj_lst = [[]for _ in range(N + 1)]

    for _ in range(E):
        a,b,c = map(int,input().split())
        adj_lst[a].append((b,c))

    inf = 1e9
    dist=[float('inf')]*(N+1)
    
    dist[0]=0

    pq = [(0,0)]

    while pq:
        cost,now = heapq.heappop(pq)

        if cost > dist[now]:
            continue

        for nxt, w in adj_lst[now]:
            new_cost = cost + w

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))


    print(f"#{tc} {dist[N]}")




    

        