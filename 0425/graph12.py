# 7465. 창용 마을 무리의 개수

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]

    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])

    def union(x, y):
        px = find(x)
        py = find(y)

        if px != py:
            parent[py] = px

    # M줄 입력
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    group = set()

    for i in range(1, N + 1):
        group.add(find(i))

    print(f"#{tc} {len(group)}")