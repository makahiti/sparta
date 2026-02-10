T=int(input())

for tc in range(1, T+1):
    N=list(map(int , input().split()))

    odd_sum=0

    for i in N:
        if i %2==1:
            odd_sum +=i

    print(f'#{tc} {odd_sum}')
