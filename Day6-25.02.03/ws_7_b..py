class Myth :
    type_of_myth = 0
    def __init__(self, name):
        self.name = name
        
        Myth.type_of_myth += 1
    
# 인스턴스가 생성될 때 , 클래스 변수가 변경
# 인스턴스가 생성 : 생성자 함수가 실행
# 클래스 변수 : 클래스 방식으로 접근

# 인스턴스 메서드 : 첫 번째 매개변수수가 인스턴스인 메서드
# 클래스 메서드 : 메서드에 @classmethod, 첫번째 매개변수가 class
# 스테틱 메서드 : 메서드에 @staticmethod, 정해진 매개변수 없음

    @staticmethod 
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

a1 = Myth('dangun')
a2 = Myth('greek&rome')

print(a1.name)
print(a2.name)

print('현재까지 생성된 신화 수 :', Myth.type_of_myth)
Myth.description()