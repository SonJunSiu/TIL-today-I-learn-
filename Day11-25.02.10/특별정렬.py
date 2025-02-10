def solve(arr, N):
    for i in range(N - 1):  # 제일 작은 값 맨 앞으로 오게 정렬해주기
        min_idx = i  # 현재 위치를 최솟값으로
        for j in range(i + 1, N):  # i 이후 최솟값 비교
            if arr[min_idx] > arr[j]:  # 지금보다 더 작은 값 찾으면
                min_idx = j  # 새로 넣어주고
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 스왑하여 최소값 앞으로

    return arr  # 정렬된 요소 반환

T = int(input())  # 테스트 케이스 개수 입력
for tc in range(T):
    N = int(input())  # 배열 크기 입력
    arr = list(map(int, input().split()))  # N개의 정수 입력받아 리스트로 저장

    new_arr = solve(arr, N)

    arrr = []  # 결과 저장할 리스트
    first = 0  # 시작 인덱스
    finish = N - 1  # 마지막 인덱스

    while first <= finish:  # 첫번째랑 마지막이랑 만날 때까지 반복
        if finish >= first:  # finish가 first보다 크거나 같을 때만 실행
            arrr.append(arr[finish])  # 큰 값을 먼저 넣어줌
        if first < finish:  # first와 finish가 같지 않을 때만 실행
            arrr.append(arr[first])  # 작은 값을 넣어줌
        first += 1
        finish -= 1

    print(f"#{tc + 1}", *arrr[:10])  # 최대 10개까지 출력