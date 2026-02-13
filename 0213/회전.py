T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))

    q=[0] * (N+M+100)
    rear = front = -1
    # arr의 원소를 맨 앞부터 차례대로 q 에 삽입한다.
    for item in arr:
        rear += 1
        q[rear] = item

    # q의 맨앞에서 원소를 꺼내서 꺼낸 원소를 다시 맨 뒤로 삽입하는 연산을# M번
    for j in range(M):
        front+=1
        item = q[front] # 하나꺼내기

        rear+=1
        q[rear] = item

        print(f"#{tc} {q[front + 1]}")


       # q의 맨 앞에 있는 원소를 출력










