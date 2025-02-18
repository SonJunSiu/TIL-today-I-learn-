def solve(arr, N) :
    for i in range(N-1) : 
        min_num = i
        for j in range(i+1, N):
            if arr[min_num] < arr[j]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]
    return arr

T = int(input())
for tc in range(T+1):
    N = int(input())

    arr = list(map(int,input().split()))

    sort_arr = solve(arr, N)

    result = []

    left = 0
    right = N - 1

    while left <= right :
        if right >= left :   # 오른쪽이 왼쪽보다 크다면 
            result.append(sort_arr[right])
            right -= 1

        if left <= right :
            result.append(sort_arr[left])
            left += 1
    