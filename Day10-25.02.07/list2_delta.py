di = [0, 1, 0, -1]  # 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]
N = 2
M = 3

i = 2
j = 3
for i in range(N):
    for j in range(M) :
        for dir in range(4) :
            ni = i + di[dir]
            nj = j + dj[dir]
            if  0 <= ni < N and 0 <= nj < M :  #리스트 바깥은 벗어나지 마
                print(ni, nj)

