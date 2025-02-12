def solve(t, p):
    N = len(t)   # 긴 문자
    M = len(p)   # 저장된 짧은 문자
    cnt = 0       # 패턴 등장 변수
    i=j=0         # 긴,짧은문자 탐색 인덱스
    
    while i < N :
        if t[i] != p[j]:    # 현재 문자가 다르면
            i = i - j + 1 # i위치 옮겨서 다시 탐색
            j = 0         # 패턴도 초기화

        else :            # 현재 문자가 맞다면
            i += 1        # 긴문자열 다음으로 이동
            j += 1        # 짧은 문자열도 다음으로 이동

        if  j == M :         # 패턴이 똑같은경우
            cnt += 1         # cnt 증가
            j = 0             # 다시 패턴도 초기화

    return (N - M*cnt) + cnt  # 최솟값
    

tc = int(input())
for testcase in range(tc):
    t, p = input().split()
    print(f'#{testcase+1} {solve(t, p)}')
