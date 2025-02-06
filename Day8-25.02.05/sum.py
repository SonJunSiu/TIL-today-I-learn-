T = int(input())

for ic in range (1, T+1) : # 테스트 케이스 개수 만큼 반복
    N, M = map(int,input().split()) # N 정수의 개수 M 구간의 개수(더해야하는)
    P = list(map(int,input().split())) # 주어지는 정수

    sum_list = [] # M의 합을 저장하는 리스트

    for i in range(N - M + 1) : # i는 연속된 M개의 숫자의 '시작 위치' 
        s = 0 # 현재구간 M개의 숫자 합을 저장함함
        for j in range (i, i+M) : #i에서시작하는 길이 M 반복
            s += P[j] #M합들을 더하고
        sum_list.append(s) # s에 이어?넣어줌.

    max_sum = max(sum_list)
    min_sum = min(sum_list)

    print(f'#{ic} {max_sum-min_sum}')

        

