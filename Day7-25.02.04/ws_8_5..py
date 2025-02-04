class Sound:
    def __init__(self, sound):
        self.sound = sound 

class Dog(Sound):
    def __init__(self):
        Sound.__init__(self, "멍멍")  

class Cat(Sound):
    def __init__(self):
        Sound.__init__(self, "야옹")  

# (Dog를 우선 상속)
class Pet1(Dog, Cat):
    def __init__(self):
        Dog.__init__(self) 

    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."

# (Cat을 우선 상속)
class Pet2(Cat, Dog):
    def __init__(self):
        Cat.__init__(self)  

    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."


print(Pet1())  
print(Pet2())  
