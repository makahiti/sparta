import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

inf = 10000000
dist = [inf] * (N + 1)
dist[1] = 0

pq = [(0,1)]

while pq:
    cost, now = heapq.heappop(pq)

    if cost > dist[now]:
        continue

    for nxt, w in graph[now]:
        new_cost = cost + w

        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

print(dist[N])