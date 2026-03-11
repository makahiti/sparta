T = int(input())

for tc in range(1, T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    
    def quickslot(A,l,r):
        if l < r:
            p = partition(A,l,r)
            quickslot(A,l,p-1)
            quickslot(A, p + 1,r)
            
    def partition(A,l,r):
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
                
                
        A[l], A[j] = A[j], A[l]        
        return j

    quickslot(arr, 0, N - 1)
    
    

    print(f'#{tc} {arr[N//2]}')

