T = int(input())

pair = list(map(int, input().strip())for _ in range())

for A, B in pair:
    s = A + B 

for tc in range(1,T+1):
    print(f'Case #{tc}: {A} + {B} = {s}')