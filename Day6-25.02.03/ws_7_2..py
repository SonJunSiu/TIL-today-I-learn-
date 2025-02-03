# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, wedith, height):
        self.wedith = wedith
        self.height = height
        
    def calculate_area(self) :
        return self.wedith * self.height


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)
