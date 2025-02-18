def f( i, N): # i 인덱스 N배열크기
    if i == N :
        #print(bit)
        s = 0 # 부분집합의 합
        for j in range(N):
            if bit[j]:
                s += A[j]
        print(s)
        print(bit)
    else :
        bit[i] = 1 # bit[i]를 1로 결정
        f(i+1, N) # 다음자리 결정하러 이동
        bit[i] = 0
        f(i+1, N)


A = [1,2,3]
bit = [0] * len(A)
f(0, len(A))