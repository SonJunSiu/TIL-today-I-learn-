def solve(N, M, arr):
    max_point = 0
    dr = [-1,1,0,0]  #상 하 좌 우 
    dc = [0,0,-1,1]

    for i in range(N) :   # 행
        for j in range(M):  # 열 
            s = arr[i][j] # 현재위치
            cnt = s  # 현재 위치의 꽃가뤼 개수

            for d in range(4) : # 상 하 좌 우 탐색
                for m in range(1, s+1) : # 1~ 현재위치 +1 상하좌우만큼
                    nr = i + dr[d] * m
                    nc = j + dc[d] * m

                    if 0 <= nr < N and 0 <= nc < M :
                        cnt += arr[nr][nc]
            
            if cnt > max_point :
                max_point = cnt
    return max_point






T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = solve(N, M ,arr)

    print(f'#{tc} {result}')

