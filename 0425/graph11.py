T = int(input())

for tc in range(1, T+1):
    N, M = map(int, (input().split())) #출석번호 개 수, # 신청서 장 수
    pair = list(map(int, input().split()))

    # 처음엔 자기 자신이 대표자
    parent = [i for i in range(N+1)]

    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])
    
    def union(x,y):
        px = find(x)
        py = find(y)

        if px != py:
            parent[py] = px

    # M 개의 신청서 처리
    for i in range(0, M*2, 2):
        a = pair[i]
        b = pair[i + 1]
        union(a,b)

        # 대표자 개수 세기
        group = set()
        
        for i in range(1, N + 1):
            group.add(find(i))


    print(f'#{tc} {len(group)}')
    



