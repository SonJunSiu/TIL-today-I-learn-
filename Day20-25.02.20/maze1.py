def start(maze): # 출발시작 위치
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j      # 16x16 미로에서 2도착
            
for _ in range(10):
    tc = int(input()) # 테스트케이스 이렇게
    maze = [list(map(int,input()))for _ in range(16)] # 1: 벽 2: 출발점 3:도착점 0: 길

    r, c = start(maze)
    stack = []
    stack.append((r, c)) # 비지티드 만들기
    visited = [[0] * 16 for _ in range(16)]
    visited[r][c] = 1

    result = 0

    while stack :
        cr, cc = stack[-1] # 현위치
        if maze[cr][cc] == 3:
            result = 1
            break # 도착했을경우
        for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
            nr = cr + dr
            nc = cc + dc 

            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] !=1 and visited[nr][nc] ==0: #이동가능한구간
                visited[nr][nc] = 1 #방문했다는 표시
                stack.append((nr,nc))
                break
        else : 
            stack.pop() # 갈수없다면? 한칸 빠꾸치기

    print(f'#{tc} {result}')


    # 강사님
def bfs(sr, sc):
    que = [(sr,sc)]
    visited = [[0]* 16 for _ in range(16)]
    visited[sr][sc] = 1 # 시작점 재방문 방지지
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    while que:
        cr, cc = que.pop(0)
        # 현재 정점과 인접한 정점 둘러보기  # 상하좌우
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 벽으로 둘러져 있기 때문에 범위검사 할 필요 x
            if maze[nr][nc] == 0 and not visited[nr][nc] : 
                que.append((nr,nc))
                visited[nr][nc] = 1

            elif maze[nr][nc] == 3:
                return 1
    # while 문이 끝나면 길이 없다는거니까
    return 0



T = 10
for _ in range(T):
    tc = int(input())
    maze = [list(map(int,input()))for _ in range(16)]
    is_find = 0 # 출발지 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                # 목적지에 도달할 수 있으면 1 못하면 0 반환
                is_find = bfs(i,j)
                break