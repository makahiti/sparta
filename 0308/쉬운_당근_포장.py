T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    ans = 1001
    
    for i in range(N-2):
        if arr[i] == arr[i+1]:
            continue
        
        for j in range(i+1, N-1):
            if arr[j] == arr[j+1]:
                continue
            
            a = i + 1
            b = j - i
            c = N - j - 1
            
            diff = max(a,b,c) - min(a,b,c)
            ans = min(ans, diff)
    
    if ans == 1001:
        ans = -1
        
    print(f"#{tc} {ans}")