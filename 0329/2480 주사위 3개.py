#같은 눈 3개 나오면 10000원+같은눈x1000원
#같은 눈 2개 1000원+(같은눈)x100원
#모두 다른 눈 나오면 (가장 큰 눈)x100원

A,B,C=map(int,input().split())

cost = 0

if A==B==C:
    cost += 10000+max(A,B,C) * 1000

elif A==B:
    cost += 1000+(A) * 100

elif A==C:
    cost += 1000+(A) * 100

elif B==C:
    cost += 1000+(B) * 100

else:
    cost += max(A,B,C)*100

print(cost)