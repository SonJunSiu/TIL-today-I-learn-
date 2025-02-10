# i 번째 들어갈 요소를 찾아서 i번 요소와 자리 바꿔주기
arr = [1, 7, 5, 8, 2, 9, 5, 4]
def selection_sort(arr) : # 요소를 오름차순 정렬
    N = len(arr)
    # 0번부터 N-1번까지 들어갈 요소 찾아서 바꿔주기
    for i in range(N) : # i : 숫자를 넣는 순서 
        # i번째로 작은 숫자 찾기 : 값이 필요한게 아니라 위치!
        min_idx = i # 처음꺼 말고 기준에서 뒤에꺼만 비교하면 되니까
        for j in range(i+1, N) :
            # 기존 최솟값과 요소를 비교 
            if arr[min_idx] > arr[j] :
                min_idx = j
        # 반복문을 완료하면, 최솟값의 위치를 찾아야하지
        arr[i], arr[min_idx] = arr[min_idx] , arr[i]
    
selection_sort(arr)
print(arr)