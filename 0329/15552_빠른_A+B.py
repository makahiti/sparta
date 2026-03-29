#내가 풀었던 코드
# T=int(input())

# pair=[list(map(int, input().split()))for _ in range(T)]


# for A, B in pair:
#     ss=0
#     ss+=A+B
#     print(ss)

#gpt가 처음에 추천한 코드
# T = int(input())

# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A + B)

#문제의도
# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 
# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

# 또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

# import sys
# input = sys.stdin.readline

#input을 이렇게 변수 선언을 하고
#input()이렇게 쓰면 시간 단축 가능