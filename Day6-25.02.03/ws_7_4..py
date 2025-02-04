# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, wedith, height):
        self.wedith = wedith
        self.height = height
        
    def print_info(self):
        print(f'Width: {self.wedith}')
        print(f'Height: {self.height}')
        print(f'Area: {self.wedith * self.height} ')
        print(f'Perimeter: {(self.wedith + self.height) * 2}')

        


shape1 = Shape(5, 3)
shape1.print_info()
