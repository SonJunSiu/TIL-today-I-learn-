class Student:
    school = 0
    def __init__(self,name):
        self.name = name

    
    def print_name(self):   # 인스턴스 메서드 : self에 인스턴스가 참조됨    
        print(f'나는 {self.name}')

    @classmethod
    def print_school(cls):  #클래스 메서드 : cls : 클래스가 참조됨
        cls.school += 1
        print(cls.school)



s1 = Student('김싸피')
s2 = Student('박싸피')

s1.print_name()
s2.print_name()

Student.print_school()

