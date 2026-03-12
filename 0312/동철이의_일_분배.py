T = int(input())
for tc in range(1,1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    max_prob = -1
 
    selected= [0]*N
     
    def probability(cnt, chance):
        global max_prob
 
        if chance <= max_prob:
            return
         
        if cnt == N:
            max_prob = max(chance, max_prob)
            return
         
        for j in range(N):
            if selected[j]:
                continue
             
            selected[j] = 1
            prob = ((matrix[cnt][j]) / 100)
            probability(cnt+1, chance*prob)
            selected[j] = 0
 
    probability(0,1)
 
    print(f'#{tc} {max_prob * 100:.6f}')