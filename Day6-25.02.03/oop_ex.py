# 객체지향 프로그래밍 vs 절차지향 프로그래밍
# 절차 지향 프로그램
# 데이터와 명령어의 순서가 중요
# 예) 로또 번호 생성 프로그램
# 1부터 45까지 숫자 중 하나 뽑아서 numbers에 넣기
# numbers의 크기가 6이 될때까지 시행
# 출력
# 번호 출력, 번호 추출, 중복검사
# 절차 지향 예시
# 중복되지 않는 숫자 6개를 저장하기 위한 데이터 선언
import random
numbers = set()
while len(numbers) < 6 :
    numbers.add(random.randint(1, 45))


print(sorted(numbers))