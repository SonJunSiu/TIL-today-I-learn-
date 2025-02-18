N = 5
arr = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(0, r+1):
        arr[r][c] = 1

for row in arr :
    print(*row)





# memo = [[0] * 101 for _ in range(101)]

# def comb(n, r):
#     if r == 0 or n == r:
#         return 1
#     if memo[n][r] != 0:
#         return memo[n][r]
    
#     memo[n][r] = comb(n-1, r-1) + comb(n-1, r)
#     return memo[n][r]

# print(comb(30,10))