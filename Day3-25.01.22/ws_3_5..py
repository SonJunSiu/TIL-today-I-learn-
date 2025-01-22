number_of_people = 0
number_of_book = 100


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
    #print(f'현재 가입 된 유저 수 : {number_of_people}')
    print(f'{name}님 환영합니다!')
    increase_user()
    return info

def rental_book(info):
    name = info['name']
    age = info['age']
    number = age // 10 # 대여권 수
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')
    


def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')




#   return info

#user = create_user('홍길동', 30, '서울')

#print(user)
#print(f'현재 가입 된 유저 수 : {number_of_people}')


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))



#info 인자에 사용될 딕셔너리는 many_user와 map을 사용해 새로운 딕셔너리를 생성한다.
#   이 때, map에 사용될 함수는 lambda로 구현한다.
#   그 결과를 rental_book 함수에 각각 전달하여 호출한다. 이 때 역시 map 함수를 사용한다.

#이부분부터 도저히 모르겠습니다..........



