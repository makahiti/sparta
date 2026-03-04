T=int(input())

for tc in range(1,T+1):
    H,W=map(int,input().split())
    field=[list(input())for _ in range(H)]
    command_cnt= int(input())
    command=input()

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    tank = ['^', 'v', '<', '>'] #방향 묹자 배열 (방향 인덱스와 대응)

#전차 초기 위치, 방향 확인
#명령 하나씩 순서대로 처리
#발사(S),이동(UDLR)순서대로 처리

    for i in range(H):
        for j in range(W):
            if field[i][j] in tank: #전차의 초기 위치 찾기
                x, y = i, j #전차 위치
                d = tank.index(field[i][j]) #전차 방향 (0~3)
                    #  명령 하나씩 처리
    for cmd in command:

        # 방향 전환 명령 ex)SRSSRRUSSR 중에서 찾으면
        if cmd == 'U':
            d = 0
        elif cmd == 'D':
            d = 1
        elif cmd == 'L':
            d = 2
        elif cmd == 'R':
            d = 3
        else: #S 일때
            #전차가 바라보는 방향으로 한 칸 앞부터 검사
            bx = x + di[d]
            by = y + dj[d]

            # 맵 안에 있는 동안 계속 직진
            while 0 <= bx < H and 0 <= by < W:

                # 벽돌벽이면 부수고 종료
                if field[bx][by] == '*':
                    field[bx][by] = '.'
                    break

                # 강철벽이면 그냥 종료
                elif field[bx][by] == '#':
                    break

                # 아무것도 아니면 계속 직진
                bx += di[d]
                by += dj[d]

            continue  # 발사는 이동 처리 안 하고 다음 명령으로

        #이동 명령 공통 처리

        # 먼저 전차의 방향을 바꿔준다
        field[x][y] = tank[d]

        # 이동하려는 다음 위치
        nx = x + di[d]
        ny = y + dj[d]

        # 맵 안 + 평지('.')일 때만 이동
        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == '.':
            field[x][y] = '.'        # 원래 자리는 평지로
            x, y = nx, ny            # 위치 갱신
            field[x][y] = tank[d]    # 새 위치에 전차 표시

           
    print(f"#{tc}", end=" ")
    for row in field:
        print("".join(row))

# "".join(row) 
# print("".join(row))

# row는 리스트라서 그대로 출력하면 이렇게 나온다  ['.', '*', '.', '.', '>'] 

# 문제에서 원하는 건: .*..>
#"".join 으로 사이 빈칸을 없애고 문자열로 출력


    # print(W,H)
    # print(field)
    # print(command_cnt)
    # print(command)
    #입력 잘받은거 훌륭하고
    