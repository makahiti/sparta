def infix_to_postfix(expression):
    precedence = {'+': 1, '*': 2}
    stack = []
    result = []
    
    for char in expression:
        if char.isdigit():  # 숫자는 결과에 바로 추가
            result.append(char)
        else:  # 연산자는 스택에서 처리
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                result.append(stack.pop())
            stack.append(char)
    
    while stack:
        result.append(stack.pop())  # 스택에 남아있는 연산자들 처리
    
    return ''.join(result)


def evaluate_postfix(postfix):
    stack = []
    
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '*':
                stack.append(a * b)
    
    return stack[0]  # 최종 결과


# 입력 처리
T = 10  # 10개의 테스트 케이스
for _ in range(T):
    length = int(input())  # 길이 (사용하지 않음)
    expression = input().strip()
    
    # 1. 중위 표기식 -> 후위 표기식 변환
    postfix_expression = infix_to_postfix(expression)
    
    # 2. 후위 표기식 계산
    result = evaluate_postfix(postfix_expression)
    
    print(result)
