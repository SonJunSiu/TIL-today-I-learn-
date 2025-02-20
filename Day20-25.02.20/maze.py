def bfs(i, j, N):                           #시작위치 i,j, 크기 N
    visited = [[0]*N for _ in range(N)]     # visitied생성
    q = []                                  # que 생성
    q.append([i,j])                         # 시작점 인큐
    visited[i][j] = 1                       # 시작점 인큐 표시
    while q:                                # 큐에 남은 칸이 없을때까지 진행
        ti, tj = q.pop(0)                   # t <-디큐
        if maze[ti][tj] == '3' :            # t에서 할일 출구(3)에 도착하면 1 아니면 0
            # return 1                        
            return visited[ti][tj] -2 # 입구에서 출구 사이의 빈칸 수
          # t에 인접 w중, 인큐되지 않은 곳이면 
        for di, dj in [[0,1] , [1,0],[0,-1],[-1,-0]]:         
            wi, wj = ti +di, tj + dj 
            # 미로를 벗어나지 않고, 벽이 아니고, 
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != '1' and visited[wi][wj] == 0:                                      
                q.append([wi,wj])  # 인큐, 표시
                visited[wi][wj] = visited[ti][tj] +1





def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)] # 미로의 크기

    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')


# 강사님 코드
def bfs(r, c): # 2차원 배열이기 때문에 start 가아니라 좌표로 주어짐
    que = [(r,c, 0)] # 0은 출발지에서 걸리는거리
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while que :
        cr, cc, dist = que.pop(0) # 현재 r,c 의 위치
        if maze[cr][cc] == 3: # 목적지
           return  dist -1
        # 현재 위치에서 갈 수 있는 방향 >> 상하좌우
        for d in range(4):
            nr = cr + dr[d] #현재방향에서 dr의d
            nc = cc + dc[d]   # nr nc 가 0임 갈수있는길
            # 갈 수 있는 길은 상하좌우 범위 안에 있으면서 벽이 통로(0) 또는 목적지(3) 이면서 방문하지 않은 정점
            if 0 <= nr < N and 0 <= nc < N:    
                if maze[nr][nc] != 1 and not visited[nr][nc]: # 1일아니면(벽) 다 집어느라
                    que.append((nr,nc, dist+1))
                    visited[nr][nc] = 1

    
    return  0 # 다 돌았는데 못찾았을때






T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    # 출발지 찾아서 bfs 수행하면 최단거리 구하기 가능
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = bfs(i, j)

    print(f'#{tc} {result}')



