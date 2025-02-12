def bruteforce(p, t):

    N = len(t)
    M = len(p)

    i = j = 0

    while i < N and j < M :
        if t[i] != p[j] : # j 는 항상 0이다?
            i = i - j + 1 # i - j 비교 시작했던 위치
            j = 0
        else :
            i += 1
            j += 1

    if j==M :
        return(i-j)          # 패턴의 시작 인덱스
    else :
        return(-1)           # 패턴이 없는 경우

t = 'AATTTTAATTTT'
p = 'TTTTAA'

print(bruteforce(p, t))


