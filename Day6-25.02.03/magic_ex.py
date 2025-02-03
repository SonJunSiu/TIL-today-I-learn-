class Student : 
    def __init__(self, name, grade):
        self.grade = grade
        self.name = name
#매직메서드 >> 특정 동작을 위한 메서드
    def __lt__(self, other) :
        return self.grade < other.grade
    
    def __str__(self):
        return f' 저는 {self.grade}학년 {self.name}입니다.'

a = Student('김싸피' ,3)
b = Student('홍길동', 24)
print(a < b)

print(a)