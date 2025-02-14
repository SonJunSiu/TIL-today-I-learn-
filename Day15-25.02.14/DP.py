# 동적계획법  (Dynamic programming)

def fibo(n):
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 10] + 2 * f[i - 20]

    return  f[n]

print(fibo(20))

