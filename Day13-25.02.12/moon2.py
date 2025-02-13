def solve(arr, N):
    lenght = 1
    for x in range(1, 101):
        for i in range(N):
            for j in range(N - x + 1):  # 회문이 들어갈 조건
                for k in range(x // 2):
                    if arr[i][j + k] != arr[i][j + x - 1 - k]:
                        break
                else:
                    if lenght < x:
                        lenght = x

    for y in range(1, 101):
        for i in range(N):
            for j in range(N - y + 1):
                for k in range(y // 2):
                    if arr[j + k][i] != arr[j + y - 1 - k]:
                        break
                else:
                    if lenght < y:
                        lenght = y

    return lenght


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [input() for _ in range(N)]  # 배열 받기
    result = solve(arr, N)
    print(f'#[tc] {result}')