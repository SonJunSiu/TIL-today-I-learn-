T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    P = list(map(int,input().split()))

    max_sum = P[0]
    min_sum = P[0]

    for i in range(1, N) :
        if max_sum < P[i] :
            max_sum = P[i]

        if min_sum > P[i] :
            min_sum = P[i]

    print(f'#{tc} {max_sum - min_sum}')