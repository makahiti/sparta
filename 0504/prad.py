
    adj_list = [[]for _ in range(V+1)]

    # 인접리스트에 C값 넣기
    for _ in range(E):
        a,b = (map(int,input().split()))
        adj_list[a].append(b)
        adj_list[b].append(a)

        # 양방향 연결, 둘다 1씩 증가

