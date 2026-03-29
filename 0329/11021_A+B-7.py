import sys
input=sys.stdin.readline

T=int(input())
pair=[list(map(int,input().split()))for _ in range(T)]

for tc in range(1, T+1):
    A, B = pair[tc-1]
    ss = A + B
    print(f'Case #{tc}: {ss}')