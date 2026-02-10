#인접행렬
#A=0, B=1,,, G=6
#정점의 개수는 N=7개

#adj_matrix = []
#1번 정점과 2번 정점이 인접(다른 정점을 거치지 않고 바로 연결)
#adj_matrix[1][2] = 1
#adj_matrix[2][1] = 0

#3번 정점과 4번정점이 인접하지 않음
#adj_matrix[3][4] '

def dfs(s, V):
    #dfs : 깊이 우선 탐색
    #그래프의 모든 정점을 빠짐엇이 한번씩 모두 탐색
    #내가 이전에 방문 했는지 안했는지 여부를 확인
    visited = [0] * V
    #visited[5] == 1 ==> 5번정점을 방문한적이 있다.
    #visited[6] == 0 ==> 6번정점을 방문한적이 없다.
    
    #돌아올 길을 저장(기억)할 스택
    stack = []

    #시작 정점 S를 방문했다 처리 
    visited[s] = 1
    print(s)

    #현재 내가 방문하고 있는 정점 번호 v
    v=s
    #그래프 탐색 시작
    while True :
        #현재 내가 있는 정점 번호는 v
        #v와 인접한 정점(w)이 있나 없나 확인 => 있다면 이전에 방문 했나 안했나확인
        #방문 가능하면 방문한다.

        for w in range(V):
            #v와 w가 인접하고, w를 이전에 방문한적이 없으면 방문한다.
            if adj_matrix[v][w] and not visited[w]:
                #w는 갈 수 있다.
                #방문처리, w정점에서 필요한 작업을 한다
                #w에서 더 이상 갈 길이 없으면 v로 돌아와야하니 
                # v를스택에 저장
                stack.append(v)
                #w를 방문했다거 처리
                visited[w] = 1
                # w정점에서 할 일
                print(w)
                #print(w)
                v=w