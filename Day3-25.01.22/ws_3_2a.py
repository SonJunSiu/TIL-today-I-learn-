number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()

    info = {
        '이름' : name,
        '나이' : age,
        '주소' : address,
        '유저 번호' : number_of_people
    }
    print(f'{__name__}님 환영합니다')
    return info
user = create_user('홍길동', 25, '서울시 강남구')
print(user)
