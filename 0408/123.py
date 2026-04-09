from heapq import heappop, heappush



def prim(tax):
    pq = [(0,0)]
    visited = [0] * N
    min_cost = 0

    while pq:
        cost, node = heappop([pq])

        if visited[node]:
            continue

    visited[node] = 1
    min_cost += cost

    for next_node in range(N):
        if visited[next_node]:
            continue

        # node -> next_node 거리계산
        # (x좌표 차이 ** 2) + (y좌표 차이 ** 2)) * tax
        next_cost = ((x_list[next_node] - x_list[node])) ** 2 +(y_list[next_node] - y_list[node **2]) * tax

        heappush(pq, (next_node))

    return round(min_cost)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax=float(input())

