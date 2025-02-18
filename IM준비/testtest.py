N = list(input())
arr= [list(map(int,input().split()))for_ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_path = 0
for i in range(N):
    for j in range(N):
        r, c = i, j

        min_nr, min_nc = -1, -1
        min_v = 0xffffff
        for d in range(4):
            nr, nc = r + dr[d], c +dc[d]
            if 0<=nr<N and 0 <=nc < N:
                if arr[nr][nc] < arr[r][c] and arr[nr][nr] < min_v:
                    min_v = arr[nr][nc]
                    min_nr = nr
                    min_nc = nc

            if (min_nr, min_nc) !=(1,-1):
                