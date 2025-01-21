lst = [1,2,3]
lst2 = [1,2,3]
print(lst == lst2) # 값 비교, 요소가 같은 값을 가지는지 비교
print(lst is lst2) # 객체 비교, 두 객체가 같은 객체인지 비교교
# 파이썬은 모든 것이 객체!
a = 105678
b = 105678
print (a == b) # 참고 : 숫자는 상수영역이라 같은 객체 가져다 씀씀
print (a is b)

# None 비교
x = [] #데이터가 없음
if not x == False :
    print('x는 False')

if not None == False :
    print('None는 False')

if x is None :
    print('x는 None')

#상당히 어렵다...

#논리연산 >>> 제어문에서 많이 사용

# and, or , not 
# 피연산자가 논리값이여야 함
# 비교연산의 피연산자 >>> 숫자        3 > 5
# 논리연산의 피연산자 >>> 논리값      True and True
# ex] 남자 이면서 성인이냐? >>> 군입대
if 남자 and 성인 :
    군입대

# and : 피연산자가 모두 True일 때만 결과가 True
# or : 피연산자 둘 중에 하나라도 True 이면 True 다!
# not :(단일항연산) : 피연산자의 결과를 반전한 결과
# True and True : 둘 다 True 니까 True
# True and False : 둘 다 True 아니니까 False
# False and False : False
# False and True : False

# True or False : True
# False or False : False               0 >>> False 그외 >>> True 단축평가를 잘 알아두자
