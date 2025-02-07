# # N * N 정사각형의 행렬에서
# # 상하좌우의 합 중에 최대값 찾기

# 요소 하나씩 돌면서 상하좌우로 비교하기
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

N = len(arr)

# 상하좌우 4방향에 접근을 위해서 변화량배열(델타)선언
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

K = 2

for r in range(N):
    # print(arr[i]) : 리스트
    for c in range(N):  # i행의 j번 요소
        print(arr[r][c])

        # 각 요소마다 상하좌우에 있는 요소에 접근
        sum_v = arr[r][c]

        for d in range(4):  # d : 방향을 나타내는 변수, 0 : 상, 1: 하 , 2:좌, 3: 우
            # 현재좌표 (r,c)
            # 보려는 좌표
            for a in range(1, K+1) : # 어떠한 방향으로 몇칸갈지 정하는 반복문
                nr = r + dr[d]*a   # 다시 질문하자 이부분은 ㅋㅋ
                nc = c + dc[d]*a
            if (0 <= nr < N) and (nc >= 0 and nc < N):
                # nr과 nc가 정상범위
                # print(arr[nr][nc])
                sum_v += arr[nr][nc]
        print(sum_v)

# arr = [[x for x in range(s, s+5)] for s in range (1, 25, 5)]
#
# print(arr)