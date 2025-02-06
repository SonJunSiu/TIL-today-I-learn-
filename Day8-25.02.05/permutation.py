# 순열(permutation) < 수열의 모든 경우의 수
# 완전탐색
# 모든 경우의 수를 탐색하기
# 부분집합, 조합, 순열, DFS, BFS
arr = [1,2,3]
N = len(arr)


perm = [0] * N
# perm의 0번 칸에 넣을 수 있는거 다 넣어보기
for i in range(N):
    perm[0] = arr[i]
    for j in range(N) :
        #j는 i와 같으면 안됨, 같아도 되는건 중복순열
        if i == j : continue
        perm[1] = arr[j]
        for k in range(N):
            if k == i == j : continue
            perm[2] = arr[k]
            print(perm)


# 요소가 3개일때 모든 부분 집합을 구할 수 있다.
check = [0] * N
for i in range(2) :
    check[0] = i
    for j in range(2) : 
        check[1] = j
        for k in range(2) :
            print(check)