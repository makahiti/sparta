T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    student_score = [list(map(int, input().split())) for _ in range(N)]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
 
    lst = [] # 모든 학생의 총점
    K_score = 0 # K번 학생 점수
    for i in range(len(student_score)): # 점수 계산
        s = student_score[i]
        total_score = s[0]*0.35 + s[1]*0.45 + s[2]*0.2
        lst.append(total_score)#학생들의 점수를 리스트에 추가
 
        if i == K-1: #K는 1번부터, 리스트 인덱스는 0부터, K=3 == i[2]
            K_score = total_score
 
    lst.sort(reverse=True) # 점수 내림차순 정렬
    K_idx = lst.index(K_score) # K 번 학생 위치 구하기 .index 메소드를 통해 처음 등장하는 인덱스 반환
 
    K_grade = grade[K_idx//(N//10)] #N//10 = 한 학점당 들어갈 학생 수
                                    #grade 리스트 안에서 인덱스 호출
 
    print(f'#{tc} {K_grade}')