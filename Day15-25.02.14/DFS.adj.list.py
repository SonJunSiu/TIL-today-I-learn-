data = list(map(int,input().split()))
adj = [[0] * (V + 1) for _ in range(V+1)]
for i in range(0, E*2, 2):
    a, b =(data[i], data[i+1])
    adj[a].append(b) # a랑b랑연결 되어 있다.
    adj[b].append(a)


    top = -1

    stack = [start]
    # 방문했던 정점에 재 방문하지 않기 위해서(되돌아가는거 말고) 방문표시 해야함
    visited = [0] * (V+1) # 인덱스가 정점번호, value가 방문여부 1 또는 0
    visited[start] = 1 # start에서 시작하니께
    print(start, end='  ')
    # 현재위치에서 갈 수 있는 길이 있으면 이동하기
    # while len(stack) > 0:
    while top > -1 :
        current = stack[top] # 리스트로 만들었고 맨 마지막에 추가된 요소니까 -1
        adj_lst[current]  # 각 요소가 current 정점과 연결된 정점
        for v in adj_lst[current] :
            if not visited[V]:
                top += 1
                stack[top] = v
                visited[v] = 1
                print(v, end=' ')
                break
        else :
            top -= 1 # pop
