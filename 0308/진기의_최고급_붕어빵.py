T=int(input())

for tc in range(1,T+1):
    N, M, K=map(int, input().split())
    arr = list(map(int, input().split()))

    possible = True

    arr.sort()
    
    
    for i in range(N):
        time = arr[i]
        bread = (time // M) * K
        
        if bread < i + 1:
            possible = False
            break
    
    if possible:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")

# print(N,M,K)

#N=오늘 올 손님의 숫자
#M=붕어빵이 만들어지는데 걸리는 시간
#K=M초의 시간을 들이면 만들 수 있는 붕어빵의 개수
#각 사람이 언제 도착하는지 초 단위로 나타냄