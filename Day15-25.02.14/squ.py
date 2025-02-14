# 재귀
def solve(n) :
    n = n // 10  # 10의 배수 단위로 변환
    if n == 1 :
        return  1
    if n == 2 :
        return  3
    f = [0] * (n + 1)
    f[1] = 1  # 하나일때는 한개만 들어가고
    f[2] = 3  # 두개부터 3개가 가능함

    for i in range(3, n+1): # 3번째부터 계산시작함
        f[i] = f[i-1] + 2 * f[i-2]   # -2 하면 두개가 들어가니까 가로세로 고려해서 *2 해야함
    return f[n]

# 점화
def solve2(N):
    N = N // 10
    memo = [0] * 30
    memo[1] = 1
    memo[2] = 3
    for i in range(3, N+1) :
        memo[i] = memo[i - 1] + memo[i - 2] * 2
    return memo[N]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = solve(n)

    print(f'#{tc} {result}')
