# 재귀함수 : 반복문이랑 비슷하기도 하구
#           큰 문제를 해결할 때 작은 문제의 결과가 필요한 경우 사용
# 제곱수 구해보기 ex) 3**8
def my_expo(base, n) : 
    if n == 0 :
        return 1
    #my_expo의 결과는 my_expo(base, n-1) * base
    return  my_expo(base, n-1) * base
print(my_expo(3, 789))

def recur_example(number):
    '''
        함수(2) 실행
            number에 2 할당
            if 2 == 1 조건문 만족하지 않음
            else문 2 + 함수(2-1) 
                결과를 알기위해서는 함수(2-1)의 실행 결과가 필요

                함수(2-1) 실행
                    number에 1 할당
                    if 1 == 1 조건문 만족하므로 1 반환
            
            else문의 2 + 함수(2-1)중, 함수(2-1)의 실행결과가 1임을 알게되었음 
            2 + 1 반환
        결과 : 3  
    '''
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
def power(base, exponent):
    '''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
    if  exponent == 0 :
        return 1
    else:
        return base * power(base, exponent -1)
    
result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8

# 모든 자릿수 더하기 함수
# 함수가 한번 수행할때 명확하게 정으
# 맨 끝자리 떼어내서 나머지 결과에 더하기 
# 42133 % 10 하면 3 나옴 

def sum_of_digits(number):
    '''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
    if number < 10 :
        return number
    else:
        return (number % 10) + sum_of_digits(number // 10)
    
result_3 = sum_of_digits(456456456456456456456456456456456456)
print(result_3) # 1 + 2 + 3 = 6

'''
학습 목표
재귀 함수의 기본적인 개념과 작동 방식을 이해한다.
재귀 함수를 사용하여 기본적인 수학 문제(거듭 제곱, 자릿수 합 등)를 해결할 수 있다.
재귀 함수의 기초 구조를 익히고, 각 단계에서 함수 호출이 어떻게 작동하는지 파악할 수 있다.

학습 개념
재귀 함수 (Recursive Function)
정의: 재귀 함수는 자기 자신을 호출하는 함수입니다. 일반적으로 종료 조건이 있으며, 이 조건을 충족하면 더 이상 자신을 호출하지 않고 값을 반환합니다.
기본 구조:
def function_name(parameters):
    if 종료_조건:
        return 종료값
    else:
        return some_operation(function_name(다음_매개변수))
작동 방식:
함수는 처음 호출될 때부터 종료 조건에 도달할 때까지 반복적으로 호출됩니다.
종료 조건에 도달하면, 함수가 반환되기 시작하여 각 호출이 완료됩니다.

학습 방향
기초 재귀 함수 작성 연습: 종료 조건이 명확한 간단한 재귀 함수를 작성해 보고, 함수 호출의 순서와 값을 이해합니다.
수학적 문제 해결: 재귀를 통해 기본적인 수학 문제(거듭 제곱, 자릿수 합 계산 등)를 풀어보며, 각 단계에서의 함수 호출 흐름을 분석합니다.
디버깅 훈련: 재귀 함수의 호출 과정을 디버깅하여, 각 호출이 어떤 값을 반환하고 어떻게 작동하는지 시각적으로 확인합니다.

문제
파이썬에서 재귀함수를 정의하는 방법을 연습하고자 한다. 예시 코드를 참고하여 요구 사항을 만족하는 코드를 작성하시오.
요구사항
base(밑)와 exponent(지수)를 인자로 받아 제곱 값을 반환하는 함수 power를 작성하시오. 
자연수를 입력받아, 각 자릿수의 합을 반환하는 함수 sum_of_digits를 작성하시오.
'''