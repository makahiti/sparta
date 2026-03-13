T = int(input())

for tc in range(1, T+1):
    N = float(input())

    bin = '' # 0. 을 제외한 소수 부분만 문자열로 저장

    cnt = 0 # 지금까지 만든 이진수 자릿수를 세는 변수 

    while cnt < 13 and N != 0: