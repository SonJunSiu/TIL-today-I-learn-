import sys
sys.stdin = open('input_ladder1.txt', 'r')
# sys.stdout = open('output_laddr1.txt'. 'w')


def solve() : # 목적지(2)에 도달하는 시작 X를 반환하는 함수
    # 상 : 0, 좌 : 1, 우 : 2
    d = 0   # 시작 방향은 위쪽
    dr = [-1,0,0] # 상
    dc = [0,-1,1]  # 좌우

    r = 99
    c = -1
    # 시작 c 찾기
    for i in range(100) :
        if ladder[r][i] == 2 :
            c = i
            break
    # 움직이기
    while True :
        if r == 0 :
            break
        # 현재 위쪽으로 올라가고 있으면 얖 옆 확인하기
        if d == 0 :
            # 현위치 : (r,c)
            if c > 0 and ladder[c][c-1] == 1: # 좌에 1 이 있다면
                d = 1 # 좌로 방향을 꺽습니다

            elif c < 99 and ladder[c][c+1] == 1: # 우에 1이 있다면
                d = 2 # 우회전
        else:         # 현재 좌 또는 우로 이동하고 있는 경우 # 위쪽으로 가는 길이 있는지 확인
            if ladder[r-1][c] == 1:
                d = 0

        r += dr[d]
        c += dc[d]
    # while문이 끝났을때 x좌표는 c
    return c

def solve2() :
    r = 99
    c = -1
    for i in range(100) :
        if ladder[r][c] == 2:
            c = i
            break
    while True :  # r의 좌표를 1씩 줄이는 반 복 문
        if r == 0:
            break
        # 줄이기 전에 양 옆에 갈 수 있는 길이 있으면 끝까지 가기
        if c > 0 and ladder[r][c-1]:
            while c > 0 and ladder[r][c-1] == 1:
                c -= 1
        elif c < 00 and ladder[r][c+1]:
            while c < 99 and ladder[r][c + 1] == 1:
                c += 1

        r -= 1


T = 10
for _ in range(T) :
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    result = solve()

    print(f'#{tc} {result}')

