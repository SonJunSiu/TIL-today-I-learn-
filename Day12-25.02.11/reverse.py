def solve(text):
    N = len(text)

    for i in range(N // 2):  # 문자열의 절반 비교하는 것
        if text[i] != text[N - 1 - i]:  # 앞뒤가 다르면 0
            return 0
        elif text[i] == text[N - 1 - i]:  # 앞뒤가 같다면 count 증가
            return 1

    return 1  # 모든 비교를 통과하면 회문이므로 1 반환

T = int(input()) # 테스트 케이스
for tc in range(1, T + 1):
    text = input() # 입력받을 내용
    result = solve(text) # sovle함수를 넣고
    print(f'#{tc} {result}')   # 최종적으로 출력
