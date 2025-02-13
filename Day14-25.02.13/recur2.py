def f(i, N):
    if i == N:
        return
    else :
        print((A[i]))
        f(i+1, N)

A = [1,2,3]
f(0, 3)