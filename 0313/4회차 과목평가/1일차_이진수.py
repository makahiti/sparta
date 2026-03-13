T = int(input())

for tc in range(1, T+1):
    N, A = input().split()
    N = int(input(N))

    result = ""

    for c in A:
        result += format(int(c, 16),'04b')

    print(f'#{tc} {result}')

