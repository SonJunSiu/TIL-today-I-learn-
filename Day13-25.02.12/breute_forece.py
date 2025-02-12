# 패턴찾기 고지식한
t = 'Hello, nice to meet you mammm'
p = 'mamm'

N = len(t) # 타겟의 길이
M = len(p) # 찾고자 하는 패턴의 길이
# 0 1 2 3 4 5 6 7 8 9
# target 0 0 0 0 0 0 0 0 0 0
# pattern            a a a a
for i in range(N-M+1):
    # i번에서 시작하는 길이 M짜리 문자열 검사하기
    for j in range(M):
        #p[j] < --- > t[i+j]
        # 같으면 진행, 다르면 종료
        if p[j] != t[i+j] :
            break
    else : # 브레끼 한번도 안걸리면 실행되는 코드! # 여기서 브레이크가 안걸리면 패턴과 다른 요소가 없다! = 패턴 찾았ㄷ따!
        print('패턴 찾음')
        break
else : # 바깥 반복문에서 패턴을 못찾았을때
    print('그런건 없어요')