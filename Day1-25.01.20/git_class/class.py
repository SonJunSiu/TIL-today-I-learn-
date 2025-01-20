greeting = 'Hello'
# 1. 인덱싱 가능
print(greeting[3])

#greeting[1] = 'a'
#문자열은 변경불가! (immutable)
greeting = 'Hallow'
print(greeting)
#이케는 바꿔도 가능

lst = [1, 2, 3, 4, 5]
lst[4] = 100
print(lst)
# 숫자는 변경가능 (mutable) list는 가변형이라 가능

# sequence 반복문에서 많이 사용
for ch in  greeting:  # greeting에서 꺼내서 for in에 하나씩 넣어줌
    print(ch)

# 리스트의 각 요소를 반복문을 이용해서 출력하는 방법
# 1. 
for el in lst :
    print(el)

#lst[0]
#lst[1]
#lst[2]   #이건 좀 아마 같잖 ㅋㅋ 그래서

#2. range와 indexing 활용하기
for i in range (5) :
    print(lst[i])

for i in range(len(lst)) : # 1, n+1
    print(lst[i])

#IndexError : list or string index out of range 길이 설정값 보다 리스트가 작을 시

num = 10 
print(num[2])

#TypeError: 'int' object is not subscriptable 인트 객체는 subscriptable이 아니다 = 내가 대괄호 쓰면 안되는 곳에 썻구나...

