N = 4
check = [0] * N # 퀸이 어느 열에 놓여졌는지 표시하는 배열
arr =[['0']*N for _ in range(N)]
dia1 = [0]*(2*N-1)


# row행에 퀸을 하나 놓아보기
def nqueen(row):
    # row행에서 할 수 있는 경우의 수는 모든 열에 퀸 놓아보기
    if row == N:
        for row in arr:
            print(row)
        return # 퀸 놓을 필요가 없음, 행이 끝났음
    
    for i in range(N):
        if not check[i] and not dia1[row+i]:
            arr[row][i] = 'q'
            check[i] = 1 # 놓았다는 표시
            dia1[row + i] = 1
            nqueen(row+1) # 다음행에 퀸 놓으러 가기
            # 다음열에 퀸 놓을거니까 이번열에 퀸 놓았던거 빼주기
            arr[row][i] = '0'
            check[i]
nqueen(0)
# ['q', 0, 0, 0]
# [0, 'q', 0, 0]
# [0, 0, 'q', 0]
# [0, 0, 0, 'q']
    