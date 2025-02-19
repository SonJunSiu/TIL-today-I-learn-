def solve(row, tmp_sum): # row행에서 숫자 하나고르기
    global min_v
    if tmp_sum >  min_v : # 기존 알고 있던 중간결과가 값이 더 크면
        return
    if row == N: # 모든 행에서 숫자하나씩 선택완료한 상황 # 다음행이 없다는 뜻
        if tmp_sum < min_v :
            min_v = tmp_sum
        return
    for i in range(N):
        if used[i] == 0:  # if no used[i]: 이것도 똑같다 # 이전 행에서 사용한 열 사용하지마
            # arr[row][i] # row행의 원소 하나
            used[i] = 1  # 사용했으니 사용표시
            solve(row + 1, tmp_sum + arr[row][i]) # 다음행고르러 가기
            used[i] = 0   # 사용 했으니 사용표시 지우기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= [list(map(int,input().split())) for _ in range(N)]

    # 각 행마다 모든열 선택해 보기 그 중에서 젤 작은거 고르기
    
    min_v = 1000
    # 같은 열의 값을 선택하지 못하도록 사용푯기하는 배열
    used =[0] * N # 0이면 사용 안함, 1이면 사용
    solve(0,0)
    print(f'#{tc} {min_v}')

8*8*8*8*8*8*8*8*8*8
64 * 5
320