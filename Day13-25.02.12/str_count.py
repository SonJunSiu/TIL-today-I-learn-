T = int(input())
def solve(str1, str2) :
    Alpa = {} # 딕셔너리에 각 알파벳이 몇번 나왔는지 하곺

    N = len(str1)
    M = len(str2)

    for i in range(N):
        cnt = 0
        for j in range(M) :
            if str1[i] == str2[j] : # 하나뽑아서 2에 비교해서
                cnt += 1   # 나올때마다 +1
        Alpa[str1[i]] = cnt # 여기까지 딕셔너리 값 완성?

        max_point = 0
        for key in Alpa: # Alpa의 key 범위에서
            if Alpa[key] > max_point : # 저 안에 Alpa값이 max보다 크다면
                max_point = Alpa[key] # 저장
    return max_point


for tc in range(1, T+1) :
    str1 = input().strip()   # 패턴
    str2 = input().strip()   # 텍스트
    result = solve(str1, str2)
    print(f'#{tc} {result}')


