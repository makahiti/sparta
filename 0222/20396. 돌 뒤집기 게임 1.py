T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        idx = i - 1              
        color = stones[idx]     

        for k in range(idx, min(idx + j, N)):
            stones[k] = color

    print(f"#{tc}", *stones)