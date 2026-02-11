T = int(input())  # 테스트 케이스의 개수

# 연산자 우선순위 설정
icp = {"+": 1, "*": 2}  # 입력 시 우선순위 (스택에 쌓을 때)
isp = {"+": 1, "*": 2}  # 스택에서 나올 때 우선순위

# 중위 표기법을 후위 표기법으로 변환하는 함수
def get_postfix(infix, N):
    postfix = ""
    stack = []

    for i in range(N):
        if infix[i].isdigit():  # 숫자인 경우
            postfix += infix[i]
        else:  # 연산자인 경우
            # 연산자 우선순위 처리
            while stack and icp[infix[i]] <= isp[stack[-1]]:
                postfix += stack.pop()  # 스택에서 우선순위가 높은 연산자를 pop하여 postfix에 추가
            stack.append(infix[i])  # 연산자는 스택에 쌓기

    # 스택에 남은 연산자들을 후위 표기식에 추가
    while stack:
        postfix += stack.pop()

    return postfix

# 후위 표기식 계산 함수
def evaluate_postfix(postfix):
    stack = []

    for char in postfix:
        if char.isdigit():  # 숫자는 스택에 넣기
            stack.append(int(char))
        else:  # 연산자일 경우
            b = stack.pop()
            a = stack.pop()
            if char == "+":
                stack.append(a + b)
            elif char == "*":
                stack.append(a * b)

    return stack[0]  # 최종 계산된 값 반환

# 테스트 케이스 처리
for tc in range(1, T + 1):
    N = int(input())  # 계산식의 길이 (실제로는 사용되지 않지만 입력받음)
    infix = input().strip()  # 중위 표기법 계산식 입력
    
    # 중위 표기법을 후위 표기법으로 변환
    postfix = get_postfix(infix, N)

    # 후위 표기식을 계산하여 결과 출력
    result = evaluate_postfix(postfix)

    # 결과 출력
    print(f"#{tc} {result}")
