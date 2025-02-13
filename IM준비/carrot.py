def solve(N, C):  # N 당근의 총 개수 # C 당근크기
    box = []
    C.sort() # 일단 당근 크기 정렬

    over_box = (N // 2) # 한 상자에 N/2 이상 들어가면 안되니까?
    for i in range(1, N-1): # 첫번째 상자의 크기
        for j in range(i, N):
            mini_box = i
            mid_box = j - i
            big_box = N - j

            if mini_box > 0 and mid_box > 0 and big_box > 0 and mini_box <= over_box and mid_box <= over_box and big_box <= over_box:
                return True # 1개 이상은 들어있어야 하고, N/2는 초과하지 않아야한다를 나타냄봄

            biggest_box = mini_box   # 제일 많이 들어 있는 박스 찾기
            if mid_box > biggest_box:
                biggest_box = mid_box
            if big_box > biggest_box:
                biggest_box = big_box

            small_box = mini_box     # 제일 적게 들어 있는 박스 찾기
            if mid_box < small_box:
                small_box = mid_box
            if big_box < small_box :
                small_box = big_box

            ans = big_box - small_box    # 최대 - 최소 차이

            return result.append(ans)
        else :
            result.append(-1)





    




T = int(input())
result = solve(N,C)