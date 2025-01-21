T = int(input())

for i in range (1, T + 1) :
    Y = input()
    year = int(Y[0:4])
    month = int(Y[4:6])
    day = int(Y[5:8])

    if month < 1 or month > 12 :
        print(-1)

    if(month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [3, 5, 8, 10] and day > 30) or (month in [1] and day > 28) :
        print(-1)

        print(f'#{T} Y({0:4}/{4:6}/{6:8})')

