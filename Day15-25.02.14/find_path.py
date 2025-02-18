def solve():
    # 0 번에서 99번으로 가는 길이 있느냐?
    # 0 번에서 시작하는 완전 탐색 >>> DFS
    stack =[0]
    visited = [0] * 100
    visited[0] = 1
    while stack:
        current = stack[-1]
        if current == 99 :
            return 1
        # 현재 정점에서 연결된 정점 정보 graph[curent]
        if graph[current][0] != -1 and not visited[graph[current][0]] :
            stack.append(graph[current][0])
            visited[graph[current][0]] = 1
        elif graph[current][1] != -1 and not visited[graph[current][1]] :
            stack.append(graph[current][1])
            visited[graph[current][1]] = 1
        else : # 연결정보 2개 다 봤는데 갈 수 있는 경로가 없다!
            stack.pop()
    # dfs 탐색 동안 목적지에 도착 못함!
    return 0

T = 10
for _ in range(T):
    tc, E = map(int,input().split())
    graph = [[-1] * 2 for _ in range(100)] # 최대 2개니까
    # 행의 인덱스 : 정점번호
    # 열 요소: 정점과 연결된 다른 정점의 번호

    data = list(map(int,input().split()))
    for i in range(0, E*2,2):
        data[i], data[i + 1]
        if graph[data[i]][0] != -1:
        # graph[2][0] = 4 # 2번정점에 첫번째는 4번이 연결되어 있다.
            graph[data[i]][1] = data[i+1]

        else :
            graph[data[i]][0] = data[i+1]


    result = solve()
    print(f'#{tc} {result}')





