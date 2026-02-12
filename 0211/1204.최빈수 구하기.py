T=int(input())

for tc in range(1, T+1):
    N=int(input())
    scores=list(map(int, input().split()))

    score_dict={}

    for i in scores:
        if i in score_dict:
                score_dict[i] +=1
        else:
                score_dict[i] = 1

    max_fq=score_dict[0]
    
    answer=0 # 밸류가 가장 큰 값의 키를 입력할 변수
   
    for j in score_dict: #최빈값(딕셔너리 안에서 밸류가 가장 큰 키)
            if score_dict[j] > max_fq: 
                max_fq = score_dict[j]
                answer=j
            
            elif score_dict[j] == max_fq: #빈도수가 같은게 있을 때
                if j > answer: #최빈값의 키보다 j의 수가 더 크면
                    answer =j #최빈값에 j 할당

    print(f'#{tc} {answer}')
        
        #score_dict 에서 밸류값이 가장 큰 키 부터 내림차순으로 프린트 