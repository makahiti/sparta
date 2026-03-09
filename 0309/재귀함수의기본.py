#0 1 2 3 4 5 5 4 3 2 1 0
#재귀호출을 사용해서 구현 

#현재 몇 번 반복(재귀호출)을 했는지 나타낼 파라미터 
def recur(num):
    #1. 종료 조건
    if num > 5:
        return
    
    #2. 재귀 호출
    print(num, end=' ')
    recur(num + 1)
    print(num, end=' ')
    
recur(0) 
    
