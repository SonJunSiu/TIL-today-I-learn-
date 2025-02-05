number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    


def create_user(name, age, address) :
    global number_of_people
    user_info = {
        'name' : name ,
        'age' : age ,
        'address' : address ,
    }
    print(f'''현재 가입 된 유저 수 : {number_of_people}
print{name}님 환영합니다!''')
    increase_user()
    return user_info

user = create_user('홍길동', 30 , '서울')
print(user)
print(f'현재 가입 된 유저 수 : {number_of_people}')
