T = int(input())

for tc in range(1,T+1):
    N,L=map(int,input().split())
    recipe=[list(map(int, input().split()))for _ in range(N)]

    #문제 답은 주어진 제한 칼로리 이하 조합중 가장 맛에대한 점수가 높은 햄버거의 점수

    max_taste = 0

    def backtracking(idx,current_kcal,current_taste):
        global max_taste
        # 백트래킹 조건
        if current_kcal > L:
            return

        #종료 조건
        if idx >= N:
            # 모든 레시피 탐색 시, 맛 점수 갱신
            max_taste = max(max_taste, current_taste)
            return

        #재귀 호출
            # 1. 현재 레시피를 선택하지 않은 경우
        backtracking(idx + 1, current_kcal, current_taste)

            # 2. 현재 레시피를 선택하는 경우
        backtracking(idx + 1, current_kcal + recipe[idx][1], current_taste + recipe[idx][0])



    backtracking(0, 0, 0)

    print(f"#{tc} {max_taste}")

