# 1 은 이동 가능한 길
# 0 은 이동 불가능한 길
# 맨 밑바닥 2로 가야한다

# 시작점에서 아래로 진행
# 그 중 좌, 우 중 갈 수있으면 방향을 바꾸고
# 다시 아래로 진행

# ex_ 2가 (99, 44) 에 있다면 어디서 시작해야 저기로 가는가

# 1. 일단 사다리에서 2가 있는 위치를 찾느다
# 2. 2에서 위쪽으로 올라오면서 길을 찾아야한다

def solve (load) :   # 2를 찾는 함수
    col_num = [] # 2가 들어갈 빈 리스트
    for i in range(100) : # 행 100회 탐색
        if load[-1][i] == 2 : # 맨 마지막 행이 2라면 
            col_num.append(i) # col.num에 추가
    return col_num

def answer_point(load) : # 2에서 시작해서 첫 지점으로 가는 함수
    r, c = 99, solve(load)[0] # 100번째(도착점) 에서 시작

    while r > 0 : #행이 1일때 위로 올라감
        if c > 0 and load[r][c - 1] == 1: # 좌로 이동한다
            while c > 0 and load[r][c - 1] == 1: # 1이 있는 동안에만
                c -= 1  # 왼쪽으로 계속 이동 -1씩 하면서
        elif c < 99 and load[r][c + 1] == 1:
            while c < 99 and load[r][c + 1] == 1:
                c += 1  # 오른쪽으로 계속 이동

        r -= 1 # 다시 위로 이동

    return c # 도착 했을때의 열 반환

for _ in range(10):
    T = int(input())
    space = [list(map(int,input().split()))for _ in range(100)] # 사다리판 만들기

    real_answer = answer_point(space) # 진짜 정답을 찾는 것
    print(f'#{T} {real_answer}')


