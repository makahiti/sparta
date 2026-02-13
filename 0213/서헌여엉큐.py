q = []

#원소 10개 추가
for i in range(1,11):
    q.append(i)

print(q)

# 원소 10개 삭제
for i in range (10):
    e= q.pop()
    print(e, end="")
print()

print(q)