#2차원 배열을 순회하는 재귀함수 만들기
N=5

arr=[[N*j+i for i in range(1, N+1)] for j in range(N)]
# 시작 i=0, j=0
# 종료 i=4 j=4
# 시작 => 종료로 가기 위해 i와 j가 어떻게 변하는가... (행 우선 순회)
# 0,0 => 0,1 => 0,2 ....=> 1,0 => 1,1
for i in range(N):
    for j in range(N):
        print(arr[i][j], end = " ")
    print()

# def myprint(i,j,N):
#     #1. 종료조건 (현재 단계를 나타내는 어떤 파라미터들):
#     if   i== N :
#         return
#     #2. 재귀호출(현재 단계에서 필요한 작업을 하고 다음 단계로)
#     #단, 다음 단계로 가면 갈수록 종료조건에 가까워 져야 한다.
#     else:
#         print(arr[i][j])
#         myprint(i+1,N)

def myprint(i,j):
    if i >= N :
        return
    
    print(arr[i][j], end=" ")
    j += 1
    if j ==N:
        i += 1
        j = 0
        print()

    myprint(i, j)

print("===============")

myprint(0,0)

