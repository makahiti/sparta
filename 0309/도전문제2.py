arr = [1, 2, 3, 4, 5, 6]
N = 3

path=[]


def recur(i,path):
    #1.종료조건
    if i == N:
        print(path)
        return
    
    for num in arr:
        path.append(num)
        recur(i + 1, path)
        path.pop
        
    #2. 재귀호출
    #i번 단계에서 할 작업을 처리 (숫자 1~6사에서 하나 고르기)
    # 다음 단계(i+1)로 재귀 호출
    #i번 단계에서 한 번 골랐던 숫자를 빼고 다시 다른 숫자를 넣을 수 있도록 처리
    
recur(0,[])