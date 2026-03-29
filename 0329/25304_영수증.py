X = int(input()) # 영수증에 적힌 총 금액
N = int(input()) # 영수증에 적힌 구매한 물건 종류 수 
pair = [list(map(int, input().split()))for _ in range(N)] # 물건가격, 개수

cost=0

for a, b in pair:
    cost += a*b

if cost == X:
    print('Yes')
else:
    print('No')