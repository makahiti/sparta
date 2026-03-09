arr = [1,2,3,4,5,6]
N=3

selected = [0] * len(arr)


def perm(i,path,selected):
    
    if i == N:
        print(path)
        return
    
    #2. 재귀호출
    #i번 단계에서 할 작업을 처리 (숫자 1~6사에서 하나 고르기)
    # 다음 단계(i+1)로 재귀 호출
    #i번 단계에서 한 번 골랐던 숫자를 빼고 다시 다른 숫자를 넣을 수 있도록 처리
    #단, 0~(i-1)단계에서 고른적이 없는 숫자여야 가능
    
    for j in range(len(arr)):
        #arr 안에서 j번 인덱스에 있는 숫자를 i번 위치에 놓겠다. 
        #j번 인덱스에 있는 숫자는 이전 단계에서 쓴 적이 없어야 한다.
        if not selected[j]:
            #j번 인덱스에 잇는 숫자 선택
            path.append(arr[j])
            #선택했다고 표시
            selected[j]= 1
            perm(i+1,path,selected)
            #순열의 i번 위치에 arr의 j번 인덱스에 있던 숫자를 빼고 다른 숫자를 넣기 위한 처리
            path.pop()
            selected[j]=0
            
            
perm(0,[],selected)