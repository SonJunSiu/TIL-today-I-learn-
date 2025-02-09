for _ in range(10) :

    tc = int(input())

    N = [list(map(int,input().split()))for _ in range(100)]


    row_sum = []
    for i in range (100) :
        row_total = 0
        for j in range(100) :
            row_total += N[i][j]

        row_sum.append(row_total)

    col_sum = []
    for j in range(100) :
        col_total = 0
        for i in range(100) :
            col_total += N[i][j]
        col_sum.append(col_total)
             
             
    digit_total = 0
    for i in range(100) :
        digit_total += N[i][i]

    reverse_digit = 0
    for i in range(100) :
        reverse_digit += N[i][99-i]

    
    max_row_sum = 0
    for i in range (100):
        if max_row_sum < row_sum[i] :
            max_row_sum = row_sum[i]

    max_col_sum = 0
    for j in range(100) :
        if max_col_sum < col_sum[j] :
            max_col_sum = col_sum[j]

    if digit_total > reverse_digit :
        max_digit_sum = digit_total

    else : 
        max_digit_sum = reverse_digit


    answer = max_row_sum
    if answer < max_col_sum :
        answer = max_col_sum 
    if max_digit_sum > answer :
        answer = max_digit_sum

    print(f'#{tc} {answer}')

        
 

    
