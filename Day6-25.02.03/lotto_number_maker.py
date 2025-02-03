import random
class LottoMaker :
    # numbers : 번호 6개 저장하는 변수
    # pcik_numbers : 숫자 뽑는 동작
    # 정렬 및 출력
    def __init__(self) :
       # 객체가 가지는 상태(속성)는 변수로 선언
       # 객체가 가지는 동작(행동)은 메서드(함수)로 선언
        self.numbers = set()
       # 인스턴스 메서드 : 첫 번째 인자가 'self'인 메서드

def pick_number(self) :
    while len(self.numbers) < 6:
        self.numbers.add(random.randint(1,45))

def sort(self) :
    self.numbers = list(self.numbers)
    self.numbers.sort()

def lotto_print(self) :
    print(self.numbers)




inst1 = LottoMaker ()
inst1.pick_numbers()
inst1.sort()
inst1.lotto_print()













a = { 'a' : 'apple'}   # a b c 모든 객체  'a'는 a의 인스턴스
b = [1,2,3,6]
c = 'hello'