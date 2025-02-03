# 아래 클래스를 수정하시오.
class Person: #클래스
    number_of_people = 0 #클래스 변수수

    def __init__(self, name, age) :     
            self.name = name
            self.age = age
            Person.number_of_people += 1

    def introduce(self) :
          print(f'제 이름은{self.name} 이고, 저는 {self.age}살 입니다.')
    



# 객체  >> 객체가 가지고 있는 특징을 클래스에 정의





person1 = Person("Alice", 25)# << 이것들이 인스턴스
person2 = Person("Bruce", 22)
person2 = Person("Cath", 30)

person1.introduce()

print(Person.number_of_people)
