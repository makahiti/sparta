T=int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num=list(input())
    # 보물상자에 적힌 숫자들을 한 글자씩 리스트로 저장
    # 예: "1B3B3B81F75E" → ['1','B','3','B','3','B','8','1','F','7','5','E']

    L=N//4 #한변에 들어가는 숫자 개수
    val =  set() #중복값을 제거해야함

    #회전은 L번만 의미 있음
    for r in range(L):
        #4개의변에서 각 숫자 생성
        for i in range(4):
            start = r + i * L # 현재 회전에서 i번째 변의 시작 인덱스
            s = '' #빈 문자열 생성
            for j in range(L): #시작 위치부터 L개를 읽어서 하나의 수를 만든다
                s += num[(start + j) % N]   # % N : 인덱스가 N을 넘어가면 처음으로 돌아가게 함 (원형 처리)
            val.add(int(s, 16))            # 16진수 → 10진수

    val = sorted(val, reverse=True) #내림차순으로 정렬, set에 저장하기 때문에 중복값이 없음
    answer = val[K - 1]#밸류에서 K -1 의 인덱스 

    print(f"#{tc} {answer}")


    #N//4 번째 
    #인덱스를 N//4 만큼?
    
