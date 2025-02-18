T = int(input())

for tc in range(1, T+1) :
    N, M  = map(int,input().split())   # N = 배열의 길이 M = M개만큼 더하는것
    arr = list(map(int,input().split()))

    sum_list = []

    for i in range(N-M+1):   
        s = 0
        for j in range(i, i+M) :
            s += arr[j]
        sum_list.append(s)

    max_list = sum_list[0]
    min_list = sum_list[0]

    for s in sum_list :
        if s > max_list :
            max_list = s
        if s < min_list :
            min_list = s
    print(f"#{tc} {max_list - min_list}")





