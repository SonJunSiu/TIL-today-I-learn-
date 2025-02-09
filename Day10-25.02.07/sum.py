for _ in range(10):   # 하아 테스트케이스 안주워졌음 ㅋㅋ
    tc = int(input())

    arr = [list(map(int,input().split()))for _ in range(100)] # 100*100 판 형성

    #행 합 구하기

    row_sum = []
    for i in range(100) : 
        row_total = 0 # 각 행 합 구하는 변수 
        for j in range(100) : 
            row_total += arr[i][j] # 순회하면서 누적값
        row_sum.append(row_total) # 누적값을 row에 넣어줌

    col_sum = [] # 각 열 합 구하는 변수
    for j in range(100) :
        col_total = 0
        for i in range(100) :
            col_total += arr[i][j]
        col_sum.append(col_total)


    digit_sum = 0  # 좌상단우하향 대각선
    for i in range(100) :
        digit_sum += arr[i][i]


    reverse_digit = 0 # 우상단 좌하향 대각선
    for i in range(100) : 
        reverse_digit += arr[i][100-1-i]

    max_row_sum = row_sum[0]          # 행 합 중 가장 큰 값 찾기
    for i in range (1, 100) : 
        if row_sum[i] > max_row_sum :
            max_row_sum = row_sum[i]

    max_col_sum = col_sum[0]   # 열 합 중 가장 큰 값 찾기
    for j in range(1, 100) : 
        if col_sum[j] > max_col_sum :
            max_col_sum = col_sum[j]
    
    if digit_sum > reverse_digit :     # 댁각선중에 더 큰 값 저장
        max_digit_sum = digit_sum
    else :
        max_digit_sum = reverse_digit

    total = max_row_sum                  # 최종적 젤 큰 값 넣을 변수
    if max_col_sum > total :         # row_sum을 선언해놨으니 열 비교
        total = max_col_sum

    if max_digit_sum > total :       #  대각선을 비교
        total = max_digit_sum

    print(f'#{tc} {total}')





    
    