def solve(ans, N, M) :
    for i in range(8):  # 행 탐색
        for j in range(N - M + 1):
            row_word = ''
            for k in range(M):
                row_word += ans[i][j+k]

            palindrome = True
            for k in range(M // 2):
                if row_word[k] != row_word[M-1-k]:
                    palindrome = False
                    break
            if palindrome:
                return  row_word


    for j in range(N): # 열 탐색
        for i in range(N - M + 1):
            col_word = ''
            for k in range(M):
                col_word += ans[i+k][j]
# 회문 확인
            is_palindrome = True
            for k in range(M // 2):  # 회문 검증
                if col_word[k] != col_word[M - 1 - k]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return col_word

    return ""






T = int(input()) # 테스트 케이스
for tc in range(1, T + 1):
    text = input() # 입력받을 내용
    result = solve(text) # sovle함수를 넣고
    print(f'#{tc} {result}')   # 최종적으로 출력