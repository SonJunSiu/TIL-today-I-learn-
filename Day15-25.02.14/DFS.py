# DFS 비선형 자료구조인 그래프의 모든 정점을 탐색하는 알고리즘
# 길을 한 방향으로 찾아가다가, 길이 없으면 되돌아가서 다시 탐색하는 방법
# 되돌아가기가 핵심 돌아갈 수 있도록, 지나온 경로를 저장 >> stack에 저장
# 현재위치: 경로상 마지막 요소 stack[top], stack[-1]
# start : 시작정점
# 시작정점에서부터 방문하는 정점을 순서대로 출력하는 함수
def dfs(start):

    stack = [start]
    # 방문했던 정점에 재 방문하지 않기 위해서(되돌아가는거 말고) 방문표시 해야함
    visited = [0] * (V+1) # 인덱스가 정점번호, value가 방문여부 1 또는 0
    visited[start] = 1 # start에서 시작하니께
    print(start, end='  ')
    # 현재위치에서 갈 수 있는 길이 있으면 이동하기
    # while len(stack) > 0:
    while stack :
        current = stack[-1] # 리스트로 만들었고 맨 마지막에 추가된 요소니까 -1
        # current 현재 위치 정점 번호
        # 현재 정점과 연결된 정점을 찾기
        for i in range(1, V+1) : # i : 정점번호 1부터 V 까지 순회하면서 현재 정점과 연결된 정점을 찾는 범위
            # ajd[current] # 우리가 봐야할 행
            if adj[current][i] == 1 and not visited[i]:  # 나랑 연결되어있으면서 방문하지 않은곳
                stack.append(i)
                visited[i] = 1 # 방문하였다.
                print(i, end=' ')
                break
        else : # for 문을 도는 동안 break에 걸리지 않았다면? 길이 없다는 뜻
            stack.pop() # 빠꾸쳐야하니까 마지막 현재 위치에서 경로에서 제거






# 1. 그래프를 저장할 때는 각 정점들이 어떻게 연결되어 있나를 저장해야한다.
# 1-1. 인접정보를 리스트 이용 공책봐라
# 간선 정보 1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
# 간선 : edge 정점 : node vertex
# 정점 개수 : V , 간선 개수: E


V = 7
E = 8
# data = '1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7'.split()

data = list(map(int,input().split()))
# 그래프를 저장하기 위해서 인접행렬 (혹은 인접리스트) 활용
adj = [[0] * (V + 1) for _ in range(V+1)] # 가로길이 V번 인덱스를 활용해야 하기 때문에 V+1개 짜리 생성

for i in range(0, E*2, 2): # 시작: 0 종료: 간선 개수*2 / 2개씩 끊어서
    a, b =(data[i], data[i+1])
    adj[a][b] = 1
    adj[b][a] = 1
for row in adj :
    print(row)

