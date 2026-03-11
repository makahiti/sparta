# 슬라이스 안 쓰고 인덱스만 사용해보기
# 교재처럼 풀면 메모리를 엄청 먹기 때문에 이런 방법 사용

arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

# 병합정렬 함수
# 정렬할 범위를 지정(인덱스)
# 시작(start) ~ 종료(end)
# 최소 크기의 부분집합이 될 때까지란 의미는 크기가 1
def merge_sort(start, end):
    # 1. 종료 조건
    # 원소가 하나 남았을 때
    # 더 이상 분할이 불가능함
    if start == end - 1:
        return start, end

    # 2. 재귀 호출
    # 두 부분으로 나누고
    # 합칠 때 정렬이 이루어진다.
    # 두 부분으로 나누는 기준은 가운데
    mid = (start + end) // 2

    # 왼쪽부분 다시 분할 후 정렬
    left_s, left_e = merge_sort(start, mid)
    # 오른쪽부분 다시 분할 후 정렬
    right_s, right_e = merge_sort(mid, end)

    # 합치면 된다.
    merge(left_s, left_e, right_s, right_e)

    # 정렬된 범위 리턴
    return start, end


# 주어진 왼쪽 부분과 오른쪽 부분을 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    # 왼쪽 부분의 가장 작은 원소가 있는 인덱스
    l = left_s

    # 오른쪽 부분의 가장 작은 원소가 있는 인덱스
    r = right_s

    # 왼쪽 부분과 오른쪽 부분을 합친 결과의 길이 N
    N = right_e - left_s
    result = [0] * N

    # result 배열에 들어갈 원소의 다음 자리 (작은 순서)
    idx = 0

    # 병합시작 (병합을 하면서 정렬이 된다)
    # 왼쪽 부분의 최소값 vs 오른쪽 부분의 최소값 비교
    # 둘 중에 작은 거 선택해서 result의 idx 위치에 넣기
    # 둘 중에 작은 거 선택해서 result의 idx 위치에 넣기
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            # 왼쪽 부분의 맨 앞에 최소값이 있다.
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            # 오른쪽부분의 맨 앞에 최소값이 있다.
            result[idx] = arr[r]
            r += 1
            idx += 1

    # 둘 중 한 부분에만 원소가 남아있는 경우
    # 남아있는 원소 주루룩 추가

    # 오른쪽만 남은 경우
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    # 왼쪽만 남은 경우
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    # result 안에는 left_s 에서 right_e 까지의 원소들이
    # 오름차순으로 정렬되어있고, 이 부분을 원본 arr 에 반영
    for i in range(N):
        arr[left_s + i] = result[i]

    print(result)

merge_sort(0, N)
print(arr)
