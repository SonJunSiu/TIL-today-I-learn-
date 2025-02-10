def snail_matrix(N) :
    T = int(input())

    N = int(input())
    space = [[0] * N for _ in range(N)]  # N * N 판 만ㄷ르기

    r, c = 0, 0    # r=행 c=열
    num = 1 
    direction = 'rigiht'

    while num <= N * N :
        space[r][c] = num 
        num += 1

        if direction == "right":
            if c + 1 < N and space[r][c + 1] == 0:  # 오른쪽 이동 가능하면 이동
                c += 1
            else:  # 이동 불가능하면 방향 변경  아래로
                direction = "down"
                r += 1  # 아래로 이동

        elif direction == "down":
            if r + 1 < N and space[r + 1][c] == 0:  # 아래 이동 가능하면 이동
                r += 1
            else:  # 이동 불가능하면 방향 변경  왼쪽으로
                direction = "left"
                c -= 1  # 왼쪽 이동
            
        elif direction == 'left':
            if c-1 < N and space[r][c-1] == 0: #왼쪽 이동 가능하면 이동
                c -= 1
            else :
                direction = 'up' # 이동 불가능 하면 방향 변경 위로로
                r -= 1 # 위쪽 이동동

        elif direction == "up":
            if r - 1 >= 0 and space[r - 1][c] == 0:  # 위쪽 이동 가능하면 이동
                r -= 1
            else:  # 이동 불가능하면 방향 변경  오른쪽으로
                direction = "right"
                c += 1  # 오른쪽 이동

    print(f'#{T} {}')




            
            


    



