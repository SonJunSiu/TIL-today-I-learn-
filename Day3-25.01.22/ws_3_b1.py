pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title = None):
    global pro_num
    data = {}
    
    data['과목'] = subject # '과목'이 key 값은 subject에 지정된 값
    data['일차'] = day
    data['제목'] = title if title is not None else "제목 없음" #어케해야하노
    data['문제 번호'] = pro_num + 1
    pro_num += 1
    return data # 이거 왜 create data 가 아닌지


result_1 = create_data('python', 3)
result_2 = create_data(subject='web', day=1, title= 'web 연습하기')
result_3 = create_data(**global_data)

print( result_1)
print(result_2)
print(result_3)