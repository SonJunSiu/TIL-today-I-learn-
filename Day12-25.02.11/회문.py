def solve(ans, N, M):
    # 가로 방향 탐색
    for i in range(N):  # 행 탐색
        for j in range(N - M + 1):  # 가능한 시작 위치
            row_word = ""  # 직접 문자열을 생성
            for k in range(M):  # 길이 M 만큼 문자 추가
                row_word += ans[i][j + k]

            # 회문 확인
            is_palindrome = True
            for k in range(M // 2):  # 회문 검증
                if row_word[k] != row_word[M - 1 - k]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return row_word

    # 세로 방향 탐색
    for j in range(N):  # 열 탐색
        for i in range(N - M + 1):  # 가능한 시작 위치
            col_word = ""  # 직접 문자열을 생성
            for k in range(M):  # 길이 M 만큼 문자 추가
                col_word += ans[i + k][j]

            # 회문 확인
            is_palindrome = True
            for k in range(M // 2):  # 회문 검증
                if col_word[k] != col_word[M - 1 - k]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return col_word

    return ""


# 입력 처리 (한 번만!)
T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N×N 크기의 글자판, 찾을 회문의 길이 M
    ans = [list(input().strip()) for _ in range(N)]  # 글자판 입력 받기

    result = solve(ans, N, M)  # 함수 호출하여 회문 찾기
    print(f"#{t} {result}")  # 결과 출력
