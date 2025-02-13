def solve(N, C):
    cnt = 1  # 연속해서 커지는 수 (1도 포함)
    max_cnt = 1  # 가장 긴 증가 구간 길이

    for i in range(1, N):
        if C[i] > C[i - 1]:  # 이전 값보다 크면 증가
            cnt += 1
        else:  # 크지 않으면 초기화
            cnt = 1

        if cnt > max_cnt :
            max_cnt = cnt
    return max_cnt




T = int(input())
for tc in range(1, T+1) :
    N = int(input()) # 당근의 개수
    C = list(map(int,input().split())) # 당근의 크기
    result = solve(N, C)
    print(f'#{tc} {result}')

