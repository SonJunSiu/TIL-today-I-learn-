# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0


class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return Animal.num_of_animal
    
    


dog = Dog()
print(f'동물의 수는 {Pet.access_num_of_animal()}마리 입니다.')
cat = Cat()
print(f'동물의 수는 {Pet.access_num_of_animal()}마리 입니다.')
