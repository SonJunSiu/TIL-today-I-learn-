# 실습 1
number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    global number_of_people
    info = {
        'name' : name,
        'age' : age,
        'address' : address,
        
    }
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    print(f'{name}님 환영합니다!')
    increase_user()
    return info

user = create_user('홍길동', 30, '서울')
print(user)
print(f'현재 가입 된 유저 수 : {number_of_people}')

#'유저 번호' : number_of_people  