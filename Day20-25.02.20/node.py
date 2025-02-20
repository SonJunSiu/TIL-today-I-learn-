def bfs(s, V):  # s: 시작 노드, V: 전체 정점 개수
    visited = [0] * (V + 1)  # 방문 배열 생성
    q = []  # 큐 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문 표시

    while q:  # 큐가 비어있을 때까지 반복
        t = q.pop(0)  # 큐에서 노드 꺼내기
        for w in adj_l[t]:  # 현재 노드 t에 연결된 모든 정점 탐색
            if visited[w] == 0:  # 아직 방문하지 않은 정점이라면
                q.append(w)  # 큐에 추가
                visited[w] = visited[t] + 1  # 거리 저장

    return visited  # 모든 노드까지의 최단 거리 반환

def solve(s, G, V):  # s: 시작 G: 목표  V: 전체 정점
    visited = bfs(s, V)  # 방문 거리 배열 가져오기
    if visited[G] > 0:  # 도착 노드 G에 방문한 적이 있으면
        return visited[G] - 1  # 최단 거리 반환
    else:
        return 0  # 도달할 수 없는 경우 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 정점  V, 간선개수 E

    adj_l = [[] for _ in range(V + 1)]  # 인접 리스트 만들기

    # E개의 간선 정보 입력
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    S, G = map(int, input().split())  # 출발 노드 S, 도착 노드 G


    print(f"#{tc} {solve(S, G, V)}")
