T = int(input())

for tc in range(1, T+1):
    V,E = map(int,input().split())
    C = list(map(int,input().split()))

    #인접리스트 만들고
    adj_list = [[]for _ in range(V+1)]

    # 인접리스트에 C값 넣기
    for i in range(0, E*2, 2):
        a = C[i]
        b = C[i + 1]

        # 양방향 연결, 둘다 1씩 증가
        adj_list[a].append(b)
        adj_list[b].append(a)

    
    # 인접리스트 완성 후 각 정점의 길이는 각 정점과 연결된 다른 정점의 개수
    # 허브 건설은 연결된 행성이 가장 많은 곳 = 연결된 정점이 가장 많은 정점
    # 연결된 정점이 가장 많은 정점이 정답

    answer = 0

    for i in range(V):
        ac = len(adj_list[i])
        answer = max(ac, answer)

    print(f'#{tc} {answer}')

    