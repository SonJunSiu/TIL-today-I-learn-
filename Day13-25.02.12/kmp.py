def kmp(t, p) :
    N = len(t)   # 텍스트의 길이
    M = len(p)   # 패턴의 길이
    lps = [0] * M

    j = 0 # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M) :
        lps[i] = j         # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
    lps[M] = j


    i = 0
    j = 0
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else :
            j = lps[j]
        if j == M:
            print(i-M, end = ' ')
            j = lps[j]
    print()