# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

# 아래 클래스를 수정하시오.
class Cat(Animal):
    def __init__(self):
        super().__init__()
        Animal.num_of_animal += 1

    def meow(self):
        print('야옹')



cat1 = Cat()
cat1.meow()
