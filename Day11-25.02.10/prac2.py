def binary_search(a, n, key) :
    start = 0
    end = n -1
    while start <= end :    #검색 구간에 1개 이상의 원소가 있으면 검색
        middle = (start + end) // 2 #기준위치계산
        if a[middle] == key : #검색 성공
            return middle
        elif a[middle] > key : #키보다 크면 왼쪽 구간 선택
            end = middle - 1
        else :                 #a[middle] < key , 키보다 작으면 왼쪽 구간 선택
            start = middle + 1
    return -1 # 검색 구간이 남아있지 않으면 검색실패
arr =[2,4,7,9,11,19,23]