T = int(input())

for i in range(T):
    A,B=map(int, input().split())
    
    print(A+B)

#########################################3
T = int(input())

pairs = [list(map(int, input().split())) for _ in range(T)]

for A, B in pairs:
    print(A + B)

#값을 밖에서 2차원배열로 받아서
# for A, B in pairs:
#     print(A + B)
#리스트를 언패킹 해서 푸는 방법도 있음