T = int(input())

N = int(input())

space = [[0] * 10 for _ in range(10)] # 공간
purple = 0

for _ in range(N):
    r1, r2, c1, c2, color = list(map(int,input().split()))

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if space[i][j] == 0 :
                space[i][j] = color

            if space[i][j] != color :
                space[i][j] = 3
                purple += 1


