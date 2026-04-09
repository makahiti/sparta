# 최단거리가 아닌, 최소 리모컨 조작 횟수
# 차윤이는 출발지에서 목적지까지 최소 조작으로 이동 가능
# RC카는 앞,왼쪽,오른쪽 90도로 이동
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, K = [list(int,input().split())for _ in range(N)]
