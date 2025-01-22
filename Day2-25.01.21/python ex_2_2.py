data = {
    '과목': 'Python',
    '구분': '실습',
    '단계': int('2'),
    '문제번호': int('3251'),
    '이름': None,
    '일차': int('22')
}

print(data)

data['단계'] = data['단계'] + '단계' # 그냥 '2단계' 도 가능


name = '딕셔너리 활용하기'
data['이름'] = name


data['일차'] -= 20


print(data)