T = 10
for tc in range(1, T+1):
    tc = int(input())
    que = list(map(int,input().split()))

    i = 1   # 감소시킬 숫자
    while True:
        if i > 5: # 1~5까지 하고 5 넘으면 초기화
            i = 1
        t = que.pop(0) - i # 첫번째 요소를 꺼냄
        if t <= 0:     #  감소한 값이 0 이하면
            que.append(0) #큐맨끝에 0 추가
            break 
        que.append(t) # 감소한 값을 큐 맨뒤에 다시 추가
        i += 1 # i값을 1 증가하면서 다음으로 이동

    print(f'#{tc}, *que')