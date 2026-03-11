arr = [7, 4, 2, 9, 11, 23, 19]

#이진검색을 하려면 정렬이 되어있어야 한다 <- 진짜 중요함 
arr.sort() 
def binary_search_while(target):
    pass
    left = 0 #검색 시작점
    right = len(arr) - 1 #검색 끝점
    
    while left <= right: #교차가 되는 순간이 탐색 못한 순간
        mid = (left + right) // 2 
        
        # 정답을 찾으면 종료 
        if arr[mid] == target:
            return mid 
        
        #arr[mid]가 target 보다 더 큰 경우(왼쪽에 위치)
        # - 왼쪽을 탐색
        if target < arr[mid]:
            right = mid - 1
            
        #arr[mid]가 target 보다 더 작은 경우(오른쪽에 위치)
        # - 오른족을 탐색
        else:
            left = mid + 1
            
print(f'9 = {binary_search_while(9)}번째 위치')