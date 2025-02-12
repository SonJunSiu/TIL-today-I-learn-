

def search(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1): # i: t  에서 패턴을 비교할 시작위치 인덱스     # 마지막 구간의 시작위치 : (N-M+1)
        for j in range(M): #p 에서 비교할 위치 인덱스ㅜ
            if t[i+j] != p[j] :
                break
        else :   # break에 걸리지 않고 for 가 끝난경우 실행
            return i
    return -1
t = 'TTTTTATTAATA'
p = 'TTA'

print(search(p, t))



