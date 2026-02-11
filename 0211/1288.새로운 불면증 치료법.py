def solve(N):
    seen_digits = set()  # 지금까지 본 숫자들을 저장할 집합
    multiplier = 0  # 몇 번째 배수를 계산했는지
    while len(seen_digits) < 10:  # 0~9 모든 숫자를 본 상태가 될 때까지
        multiplier += 1
        number = N * multiplier  # N의 배수
        seen_digits.update(str(number))  # 현재 배수의 자릿수를 집합에 추가
    
    return multiplier  # 최소 몇 번째 배수에서 모든 자릿수를 봤는지

# 입력 받기
T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    N = int(input())  # 각 테스트 케이스마다 주어진 N
    result = solve(N)
    print(f"#{t} {result}")
