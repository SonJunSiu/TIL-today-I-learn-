'''
7 8      
1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
'''
V, E = map(int, input().split())
edges = list(map(int,input().split())) # 간선을 엣지라 함
# 그래프 저장은 인접 행렬로
graph = [[0] * (V+1) for _ in range(V+1)]  # 이거 V+1개 만드는 이유 물어보기 필수!
for i in range(0, E*2, 2):
    # edges[i]번 정점과, edges[i+1]번 정점이 연결됨
    # 무향그래프니까 양방향으로 연결되어있음
    graph[edges[i]][graph[i+1]] = 1     # 1 <--> 5
    graph[edges[i+1]][graph[i]] = 1

#visited 활용해서 거리구하는법 다시 물어보기
def bfs(start):
    # 시작정점에서 인접한 정점을 순서대로 방문
    # 방문한 정점에서 다시 인접한 정점을 순서대로 방문
    # 경로를 발견한 순서대로 방문하게 된다. DFS랑 다름
    # 방문 순서를 que 에 저장하면 된다.
    que = [start] # start를 방문할꺼니까 집어넣음
    # 정점 재방문을 방지하기 위해서 visited 만들기
    visited = [0] * (V+1)
    visited[start] = 1 # 방문은 1로 표시
    while que: # 방문할 정점이 남아있는 동안 계속 방문
        current = que.pop(0) # 현재장소 경로를 되돌아 오는 개념이 아님 바로 pop 해야한다
        print(current, end=' ')

        # 현재 정점에서 방문가능한 정점을 모두 que에 담아주기
        # current에서 방문가능한 정점 정보는 graph[current] 임
        for i in range(1, V+1):
            if graph[current][i] == 1 and not visited[i]: # 여기서 1은 current와 i가 연결되어 있다는 뜻
                que.append(i) # 방문 안했으면 큐에 집어넣기?
                visited[i] = 1 # 방문 체크






# 간선 정보 1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
# 정점 개수 :V, 간선의 개수 E                                  <<< 요게 그래프 





