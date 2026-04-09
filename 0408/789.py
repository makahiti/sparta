import sys
sys.stdin = open("input3.txt", "r")

def cal_synergy(li):
    total = 0
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            a, b = li[i], li[j]
            total += arr[a][b] + arr[b][a]
    return total

def get_synergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)
    return cal_synergy(A_list), cal_synergy(B_list)

def recur(cnt, prev):
    global min_answer

    if cnt == N // 2:
        a_total, b_total = get_synergy()
        min_answer = min(min_answer, abs(a_total - b_total))  # 버그1 수정
        return

    for food_number in range(prev + 1, N):
        visited[food_number] = 1          # 버그2 수정: continue 제거
        recur(cnt + 1, food_number)       # 버그3,4 수정: 인자 전달
        visited[food_number] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_answer = 21e8
    recur(0, -1)  # 버그3 수정: 초기 인자 전달
    print(f"#{tc} {int(min_answer)}")