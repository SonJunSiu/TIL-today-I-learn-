'''
7 8
4 2  1 2  13  5 2  4 6  5 6  6 7  3 7
'''
def bfs(s, V): #시작 정점s, 마지막정점V
    visited = [0] * (V + 1) # visited 생성
    q = []             # 큐 생성
    q.append(s)          # 시작점 인큐
    visited[s] = 1       # 시작점 인큐 표시               
    while q:                     # 큐가 비워질 떄 까지 반복
        t = q.pop(0)      # 디큐해서 t에저장
        print(t)          # t정점에 대한처리
        for w in adj_l[t]: # t에 인접한 정점 w 중, 인큐되지 않은 정점이 있으면
            if visited[w] == 0:
                q.append(w) # 인큐, 인큐 표시
                visited[w] = visited[t] + 1


V, E = map(int,input().split())
arr = list(map(int,input().split()))


# 인접리스트 ------------
adj_l = [[]for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(5, V)
