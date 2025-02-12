import sys
sys.stdin = open('GNS_input.txt', 'r')
num_dict = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9
}
def bubble_sort(arr):
    for i in range(N-1): # 요소의 개수만큼 반복

        for j in range(N-1-i): # 큰 수를 뒤로 보내는 반복문
            if num_dict[arr[j]] > num_dict[arr[j+1]]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    pass
    T = int(input())
    for _ in range(T):
        tc, N = input().split()
        N = int(N)
        data = input().split()
        bubble_sort(data)
        print(f'{tc}')
        print(*data) # 언패킹 하는법 [] 이거 벗기기



#  선택정렬
def selection_sort(arr): # i번째 요소에 i번째로 작은 요소 가져와서 넣어주기
    for i in range(N-1):
        # i번 부터 N-1번까지 중에 제일 작은거 골라서 i번에 넣어주기
        # i번 위치와 바꿔주기
        min_index = i
        for j in range(i, N):
            if num_dict[arr[min_index]] > num_dict[arr[j]]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

# 카운팅 정렬
# 카운팅정렬의 제약조건 : value를 index로 사용가능해야 한다
# 최솟값과 최대값의 편차가 적아야 효율적

def counting_sort(arr):
    # 개수세기, 누적합, 자리찾아주기
    count = [0] * 10
    for i in range(N):
        idx = num_dict[arr[i]]
        count[idx] += 1
    # 누적합
    for i in range(1, N):
        count[i] == count[i-1]
    #자리찾기 # count요소가 들어갈 위치
    sorted_arr = [None]*N
    for i in range(N):
        num = num_dict[arr[i]]
        count[num] -= 1
        sorted_arr[count[num]] = arr[i]

    return sorted_arr

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    data = input().split()
    counting_sort(data)
    print(f'{tc}')
    print(*data) 

