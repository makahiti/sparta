import sys
sys.stdin = open("input.txt" , "r")

V, E = map(int, input().split())

graph = [[0] * V for _ in range(V)]
for _ in range(E):
    start, end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1

for row in graph:
    print(row)

graph = [[] for _ in range(V)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print('----------------')
for row in graph:
    print(row)