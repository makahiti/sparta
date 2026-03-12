# 병합 과정에서 역순쌍을 세는 함수
def merge_sort(arr):
    # 배열 길이가 1이면 더 이상 나눌 필요 없음
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    # 왼쪽 / 오른쪽을 각각 병합정렬
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    inv_count = left_inv + right_inv  # 왼쪽 + 오른쪽 내부의 역순쌍

    # 두 배열을 병합
    while i < len(left) and j < len(right):

        # 정상 순서이면 그대로 추가
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1

        # 역순 발생
        else:
            merged.append(right[j])
            j += 1

            # left[i] 이후 모든 원소가 right[j]보다 큼
            # 즉 len(left) - i 개 만큼 역순 발생
            inv_count += len(left) - i

    # 남은 값들 붙이기
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    wires = []

    for _ in range(N):
        A, B = map(int, input().split())
        wires.append((A, B))

    # A 기준으로 정렬
    wires.sort()

    # B 값만 따로 추출
    B_list = [b for a, b in wires]

    # 병합정렬로 역순쌍 계산
    _, ans = merge_sort(B_list)

    print(f"#{tc} {ans}")