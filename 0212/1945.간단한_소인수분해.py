T = int(input())
for tc in range(1, T+1):
    N = int(input())

    prime_num = [2, 3, 5, 7, 11]
    prime_dict = {}

    for i in prime_num:
        while N % i == 0:
            N = N//i
            if i not in prime_dict:
                prime_dict[i] = 1
            else:
                prime_dict[i] += 1

    answer = " ".join(str(prime_dict.get(p, 0)) for p in prime_num)


    print(f'#{tc} {answer}')

    #a b c d e = 승수
    #소수로 나눠질때까지 나누고
    #소수를 리스트에 저장
    #리스트 인덱스  a b c d e