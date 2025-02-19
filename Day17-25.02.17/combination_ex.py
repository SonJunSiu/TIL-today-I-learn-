arr = [1,2,3,4,5]
N = len(arr)
M = 3
# 각 요소가 조합에 포함되는지 아닌지 표시하는 배열
check = [0] * N

#check의 각 idx에 0 또는 1을 넣을거야 몇개가 포함되는지 알아야 해
def combination(idx, cnt):
    if cnt == M:
        print(check)
    if idx == N: # 정답을 못찾은 상태, 마지막인덱스까지 M개의 원소를 선택하지 모함
        # print(check)
        return
    check[idx] = 1
    combination(idx + 1, cnt + 1)  # 하나의 상태를 확정하면 다음 인덱스 결정
    check[idx] = 0
    combination(idx + 1, cnt)  # 하나의 상태를 확정하면 다음 인덱스 결정
    
        # cnt = 0
        # for i in range(N):# 요소가 몇개 포함되었는지 확인하겠따
        #     if check[i]:
        #         cnt += 1
        # if cnt == M:
        #     print(check)   여기 까지는 완전탐색 시간이 더 걸린다

combination(0, 0)
