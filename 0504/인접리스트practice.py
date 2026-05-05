T = int(input())

for tc in range(1, T+1):
    V,E = map(int,input().split())
    C = list(map(int,input().split()))

    adj_lst = [[]for _ in range(V+1)]

    for i in range(0, E*2, 2):
        a = C[i]
        b = C[i+2]

        adj_lst[a].append(b)
        adj_lst[b].append(a)

    
    answer = 0

    for i in range(1, V):
        ac = adj_lst[i]
        answer = max(ac, answer)

    print(f'#{tc} {answer}')
