# 1. 세트와 딕셔너리 초기화하기
my_set = {'가', '나', (0, 0)}  
my_dict = {
    '가': 1, 
    (0, 0): '튜플도 키값으로 사용가능'
}


for key in my_set:
    print(my_dict.get(key))

var = (1, 2, 3, 'A')  
my_dict[var] = '변수로도 키 설정 가능'

print(my_dict)
