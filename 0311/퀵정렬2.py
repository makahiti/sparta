arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

def quick_sort(A, l, r):
    if l < r:
        p = hoare_partition(A, l, r)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, r)
    
def hoare_partition(A, l, r):
    p = A[l]
    i = l
    j = r

    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    # 기존 피벗의 위치가 맨 앞 이었으므로 해당 위치에는 작은 값이 와야한다.
    # i와 j가 엇갈려 끝났으므로 j는 작은 영역 i는 큰 영역에 위치해 있다.
    # 이를 위해서 피벗 위치의 값은 j 즉 작은 영역에 위치한 값과 
    # 자리를 바꿔야 피벗의 위치 맨 앞에는 작은 값이 들어온다.
    A[l], A[j] = A[j], A[l]
    return j
quick_sort(arr, 0, N-1)
print(arr)