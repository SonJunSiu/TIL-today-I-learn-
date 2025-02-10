def solve (arr, N):
    for i in range(N-1) : # 제일 작은 값 맨 앞으로 오게 정렬해주기
        min_idx = i
        for j in range(i+1, N) : 
            if arr[min_idx] > arr[j] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr # 정렬된 요소 
    
    

            

            
# 작은거 찾아서 넣고
# 큰거 찾아서 넣고
# append 로 붙이기?
T = int(input())
N = int(input())
arr = list(map(int,input().split()))

print(f'#{T} {result}')