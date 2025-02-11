# 문자열 뒤집기
target = 'Hello'    # 중간값 찾기
N = len(target)

# 앞 뒤 쌍을 자리를 바꿔주기
# 문자열 immutable(변경불가)
target = list(target)

# 중간 전까지만 반복하면서 뒤 요소랑 자리 바꿔주기
mid = N // 2
for i in range(mid) :
    target[i] , target[N-1-i] = target[N-1-i] , target[i]

print(target)
# target : 요소가 문자열인 리스트
# 요소를 모두 하나로 합쳐서 문자열로 만들기

print(''.join(target)) # 공백을 기준으로 연결

#응용
a = 12345
a = str(a)

a = reversed(a)
print(list(a))

