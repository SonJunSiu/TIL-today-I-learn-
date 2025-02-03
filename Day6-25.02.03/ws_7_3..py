# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, wedith, height):
        self.wedith = wedith
        self.height = height
    
    def calculate_perimeter(self) :
        return self.wedith * 2 + self. height * 2
        


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
