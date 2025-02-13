def solve(arr, N):
    cnt = 0  # 회문의 개수
 
    for i in range(8):  # 행 검사
        for j in range(8 - N + 1):   # 회문검사하는 시작 인덱스
            for k in range(N // 2):  # 반으로 나눠서 비교
                if arr[i][j + k] != arr[i][j + N - 1 - k]:  # 가로 비교
                    break
            else:
                cnt += 1  # 회문이면 개수 증가
 
    for i in range(8):  # 열 검사 (따로 처리)
        for j in range(8 - N + 1):
            for k in range(N // 2):  # 반으로 나눠서 비교
                if arr[j + k][i] != arr[j + N - 1 - k][i]:  # 세로 비교
                    break
            else:
                cnt += 1  # 회문이면 개수 증가
 
    return cnt  # 총 회문 개수 반환
 
T = 10
for tc in range(1, T + 1):
    N = int(input())  # 회문의 길이
    arr = [input().strip() for _ in range(8)]  # 8x8 배열 받기
    result = solve(arr, N)
    print(f'#{tc} {result}')




