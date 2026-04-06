N = 10

#  트리로 집합을표현
p = [0] * (N + 1)

# 초기화 연산
# x 자기 자신이 대표인 집합을 만든다..
def make_set(x):
    p[x] = x

# 대표가 누군지 찾는 연산
def find_set(x):
    if x == p[x]:
        return x
    
    return find_set(p[x])

#경로 합축 버전
#x가 속한 집합의 대표를 찾는 과정에서 만나는 모든 노드의 대표를 업데이트
# 1번부터 N번까지의 모든 원소에 대해 대표를 찾는 연산을 한 번씩 하면 => 모든 원소의 대표 경로 압축

def find_set2(x):
    #x가 대표가 아니면
    if x != p[x]:
        # 경로 압축 
        p[x] = find_set2(p[x])

    return p[x]

# 두 집합을 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합친다.
# 합 칠때 주의할 점 : 각 집합의 대표가 필요하다.
def union(x, y):
    # x가 속한 집합의 대표가 누구니 ?
    king_x = find_set(x)
    # y가 속한 집합의 대표가 누구니 ?
    king_y = find_set(y)

    if king_x == king_y:
        return
    
    p[king_y] = king_x

p = [i for i in range(N + 1)]
print(p)

union(1,6)
print(p)
union(2,6)
print(p)
union(3,6)
print(p)
union(4,6)
print(p)
union(8,7)
print(p)
union(9,8)
print(p)
union(9,3)
print(p)

print("==================================")

for i in range(N+1):
    find_set2(i)

print(p)

rank = [0] * (N+1)

def union2(x, y):
    king_x = find_set2(x)
    king_y = find_set2(y)

    if rank[king_x] > rank[king_y]:
        p[king_y] = king_x
    else:
        p[king_x] = king_y

        #랭크가 같은 경우
        if rank[king_x] == rank[king_y]:
            # 큰쪽의 랭크 +1 
            # 위에서 y가 대표가 되었으니 대표 쪽 트리의 랭크 증가
            rank[king_y] += 1