# 빽 트레킹 >> 완전탐색 하면서 가능성 없는거 안하기
# 부분 집합중에 합이 10인 부분합을 출력해라
arr = [1,2,3,4,5,6,7,8,9,10]
M = 10
N = len(arr)
check = [0] * N # 요소가 0이면 idx번째 요소는 부분집합에 포함된다
# idx : 요소의 idx 요소가 부분집합에 포함되는지 안되는지 결정하는 함수
def power_set(idx, tmp_sum):
    if tmp_sum > M:   # 여기가 가지치기 빽트레킹
        return
    if idx == N :
        if tmp_sum == M:
            # print(check)
            for i in range(N):
                if check[i]:
                    print(arr[i], end=',')
            print()
        return
        # 특정상황에서 모든 경우의 수 수행해보기
    check[idx] = 1   # 부분집합에 포함 될수도 있꼬
    power_set(idx + 1, tmp_sum+arr[idx])
    check[idx] = 0   # 안될수도 있꼬
    power_set(idx + 1, tmp_sum)

power_set(0, 0)