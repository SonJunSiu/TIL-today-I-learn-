def pattern_count(p, t) :    # 패턴 등장 횟수 리턴
    pass


    N = len(t)
    M = len(p)

    i = j = 0
    cnt = 0
    while i < N :
        if t[i] != p[j] : # j 는 항상 0이다?
            i = i - j + 1 # i - j 비교 시작했던 위치
            j = 0
        else :
            i += 1
            j += 1

        if j==M :
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt

t = 'ATTATTATATTT'
p = 'TA'

print(pattern_count(p, t))


