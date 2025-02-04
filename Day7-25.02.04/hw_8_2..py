def check_number():
    try:
        num = int(input("숫자를 입력하세요: "))  
        if num > 0:
            print("양수입니다.")
        elif num == 0:
            print("0입니다.")
        else:
            print("음수0입니다.")
    except:  
        print("잘못된 입력입니다. 숫자를 입력해주세요.")

# 함수 실행
check_number()
