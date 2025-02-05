for i in range(1, 11) :
    result = 0 #초기화
    n = int(input()) #건물의 수
    h = list(map(int,input().split())) # 건물 높이
    for j in range(2, n-2) : # 2~n-3 까지 반복 앞뒤 2칸은 빼야하니까 j는 현재 검사하는 '건물'위치
        a1 = h[j] - h[j-2] #기준 건물에서 -2 
        a2 = h[j] - h[j-1] # -1
        a3 = h[j] - h[j+1] # +1
        a4 = h[j] - h[j+2] # +2
        if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 : # 좌 우 4칸 다 비어야 통과 기준건물에서 좌우 2건물 빼고 + 되야 오케이
            result += min(a1, a2, a3, a4) # 좌우 4칸 차이중에 가장 작은 값부터 값을 가지니까
    print('#{} {}'.format(i, result))


