def solve():
    # 격자 크기 10x10
    grid = [[0] * 10 for _ in range(10)]
    
    N = int(input())  # 색칠할 영역의 개수
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 해당 범위에 색칠
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 0:  # 아직 색칠되지 않은 칸
                    grid[r][c] = color
                elif grid[r][c] != color:  # 다른 색이 칠해진 칸이면 보라색으로
                    grid[r][c] = 3
    
    # 보라색 칸 세기 (값이 3인 칸)
    purple_count = sum(row.count(3) for row in grid)
    
    return purple_count


# 입력 처리
T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    result = solve()
    print(f"#{t} {result}")

#잘 모르겠어서 AI에게 도움 받앗읍니다