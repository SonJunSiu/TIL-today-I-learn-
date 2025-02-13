def solve(arr):
    max_length =1
    for i in range(N):
        is_find = False
        for M in range(N, 1, -1) : # 검사 길이 줄이는 반복문
        for j in range(N-M+1):  # 검사 시작점이동
            is_pal = True
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            is_pal = True
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:

            if is_pal:
                if max_length < M :
                    max_length = M
                is_find = True
                break
            if is_find : #
                break
T = 10
for _ in range(T) :
    tc = input()
    N = 100
    arr = [input() for _ in range(N)]
