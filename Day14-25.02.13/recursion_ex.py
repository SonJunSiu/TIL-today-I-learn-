# 반복문형태
N  = 5
arr = [0] * N    #[0],[0],[0],[0],[0] [0,0,0,0,0]
# # arr의 요소에 1,5까지 숫자 넣기
# # * 함수가 한번 호출돼서 수행하는 작업을 명확하게 해야해

# def my_func(idx, num) :
#     if idx == N :
#         return  # 함수안에서 return을 만나면 그 즉시 종료
#     arr[idx] = num
#     my_func(idx+1, num+10) 

# my_func(0, 11)
# print(arr)

def my_func2(idx):
    if idx == N:
        print(arr)
        return
    arr[idx] = 0  # arr 현재 위치에 0 저장
    my_func2(idx + 1) # 다음 위치로 이동
    arr[idx] = 1 # arr 현재 위치에 1 저장
    my_func2(idx + 1) # 다음 위치로 이동
my_func2(0)

# 큰 문제를 해결하기 위해 작은 문제를 해결하는 형태 
# 피보나치 수열 : f(n) = f(n-1) + f(n-2)
def fibo(n): #피보나치 수열에서 n번째 항을 반환하는 함수
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)
