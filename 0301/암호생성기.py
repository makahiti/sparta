T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):  # 1번부터 T번까지 반복
    N = list(map(int, input().split()))  
    # 8개의 숫자를 입력받아 리스트로 저장
    # map은 바로 인덱싱이 안되므로 list로 변환

    decrease = 1  # 감소시킬 값 (1부터 시작)

    while True:  # 암호가 완성될 때까지 반복
        first = N[0]  # 맨 앞 숫자 저장

        # 리스트를 왼쪽으로 한 칸씩 이동 (큐처럼 만들기)
        for i in range(7):
            N[i] = N[i + 1]

        # 감소값만큼 빼기
        first -= decrease

        # 만약 0 이하가 되면
        if first <= 0:
            N[7] = 0  # 맨 뒤에 0을 넣고
            break     # 반복 종료 (암호 완성)
        else:
            N[7] = first  # 감소된 값을 맨 뒤에 저장

        # 감소값을 1씩 증가
        decrease += 1

        # 감소값이 5를 초과하면 다시 1로 초기화
        if decrease > 5:
            decrease = 1

    # 결과 출력 (형식: #테스트번호 값1 값2 ... 값8)
    print(f"#{tc}", end=" ")
    for num in N:
        print(num, end=" ")
    print()  # 줄바꿈