T = int(input())

for tc in range(1, T+1):
    memory=list(map(int,input()))
    count=0 #수정 되는 횟수
    current=0 #0으로 고쳐야함

    for i in memory:
        if i != current: #i가 0이 아니면
            count+=1 #수정 횟수 +1
            current=i #바뀐 값으로 수정
    print(f'#{tc} {count}')