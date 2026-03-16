T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    tree = [[] for _ in range(N+1)] #트리 구조 저장 (부모 -> 자식)
    w = [0]*(N+1) #각 방의 보물 무게
    v = [0]*(N+1) #각 방의 보물 가치

    root = 0

    for _ in range(N):# 방 정보 입력

        # r : 방 번호
        # weight : 보물 무게
        # value : 보물 가치
        # p : 부모 방 번호

        r, weight, value, p = map(int, input().split())
    
        w[r] = weight
        v[r] = value

         # 부모가 0이면 입구방
        if p == 0:
            root = r

        # 아니면 트리에 부모 -> 자식 연결
        else:
            tree[p].append(r)

     # 최대 가치 저장 변수
    ans = 0

    def dfs(node, weight, value):
        global ans

        # 현재까지 보물 무게가 K를 초과하면
        # 더 탐색할 필요 없이 종료 (가지치기)
        if weight > K:
            return

        # 현재 방이 리프 노드 (막다른 길)
        # 더 이동할 수 없으므로 가치 비교
        if len(tree[node]) == 0:
            ans = max(ans, value)
            return

        for child in tree[node]:

            # 보물 선택
            dfs(child, weight + w[child], value + v[child])

            # 보물 미선택
            dfs(child, weight, value)

    dfs(root, w[root], v[root])
    dfs(root, 0, 0)

    print(f"#{tc} {ans}")