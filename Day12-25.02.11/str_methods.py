# int(), str()
# '5' - '0' = 53 - 48 = 5
# ord('str') : 문자열에 아스키코드에 대응하는 숫자 반환,
# chr(숫자) : 숫자의 문자 반환

# 숫자형태의 문자열을 인자로 받아서 숫자를 반환
def atoi(char):
    for i in range(len(char)):
        # char[i] # 숫자형태 문자열
        print(ord(char[i])-ord('0'))

atoi('321')
 
# 문자열을 숫자
def atoi(char):
    result = 0
    for i in range(len(char)):
        # char[i] # 숫자형태 문자열
        num = ord(char[i])-ord('0')
        result = result*10 + num
    return  result
print(atoi('321'))

def itoa(number):
    result = ''
    while number > 0 :
        remain = number // 10
        number = number % 10
        result = chr(remain + ord('0')) + result
    return result

asdf = itoa(34132)
print(asdf)