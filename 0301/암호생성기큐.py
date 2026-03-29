# T = int(input())  # 원래는 테스트케이스 개수를 입력받지만 (SWEA는 10번 고정)

for tc in range(1, 11):  # 총 10개의 테스트케이스 반복
    tc = int(input())    # 테스트케이스 번호 입력 (예: 1, 2, 3 ...)
    q = list(map(int, input().split()))  
    # 8개의 숫자를 리스트로 저장 (큐 역할)

    i = 1  # 감소값은 1부터 시작

    while True:  # 암호가 완성될 때까지 반복
        x = q.pop(0)  # 맨 앞 숫자를 꺼냄 (큐에서 dequeue)
        x -= i        # 현재 감소값(i)만큼 감소

        # 감소 후 0 이하가 되면
        if x <= 0:
            q.append(0)  # 0을 맨 뒤에 추가
            break        # 반복 종료 (암호 완성)

        q.append(x)  # 감소된 값을 맨 뒤에 추가 (enqueue)

        i += 1  # 감소값 증가

        if i == 6:  # 감소값이 5까지 갔으면
            i = 1   # 다시 1로 초기화 (1~5 반복)

    print(f'#{tc}', *q)  # 형식에 맞게 출력