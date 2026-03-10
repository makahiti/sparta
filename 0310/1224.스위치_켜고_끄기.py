N = int(input())
switch = [0] + list(map(int, input().split()))  # 1번부터 쓰기 위해 앞에 0 추가
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())

    # 남학생
    if gender == 1:
        for i in range(num, N+1, num):
            switch[i] = 1 - switch[i]

    # 여학생
    else:
        left = num
        right = num

        while left-1 >= 1 and right+1 <= N and switch[left-1] == switch[right+1]:
            left -= 1
            right += 1

        for i in range(left, right+1):
            switch[i] = 1 - switch[i]

# 출력 (20개씩)
for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()