T = int(input())
for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    def solve():

        N = len(str2) # 긴 문자열의 길이
        M = len(str1) # 짧은 문자열의 길이

        for i in range(N- M + 1) : # i : 비교하려는 시작 인덱스
            is_find = True
            for j in range(M): # 검사 인덱스
                # str1[j] 과 str2[i+j]를 비교
                if str1[j] != str2[i+j] : #다르면 검사종료
                    is_find = False
                    break
            if is_find: # True값을 유지하고 있으면 str1이 str2에 포함된다
                return 1
        return 0
result = solve()
print(f'#{tc} {result}')




