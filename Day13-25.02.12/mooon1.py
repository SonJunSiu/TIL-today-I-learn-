# arr에서 길이 M인 회문의 개수를 반환하는 함수
def solve(arr):
    result = 0
    for i in range(N): #행 순회 반복문
        for j in range(N-M+1): # 회문의 시작점 인덱스
            for k in range(M//2): # 회문검사 순서
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else :
                result += 1
            for k in range(M // 2):  # 회문검사 순서
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    break
            else:
                result += 1

    return result

T = 10
for tc in range(1, T+1):
    N = 8 # 판의 크기
    M = int(input()) # 회문의 크기
    arr = [input() for _ in range(N)]
    result = solve(arr)
    print(f'#{tc} {result})