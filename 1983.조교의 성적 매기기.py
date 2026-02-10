T=int(input())

for t in range(1, T+1):

# N은 학생 수,  K는 학점을 알고 싶은 학생의 번호
    N, K = map(int, input().split())
    S=[list(map(int,input().split())) for _ in range(N)]

    i=len(S)
    j=len(S[0])
    
    #총점 구하기 -> 학점으로 만들기 -> 
    for i in range(N):
            score=0
                score=S[i][0]*(35/100)+S[i][1]*(45/100)+S[i][2]*(20/100)
                if S[i] > 

        
