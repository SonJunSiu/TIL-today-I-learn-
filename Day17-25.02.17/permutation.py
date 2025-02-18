# 순열
arr = ['a','b','c']
N = len(arr)
perm = [None] * N

used = [0] * N # 0은 사용 안한거 1은 사용한거

# perm의 idx번째에 arr의 모든 요소에 넣어보기
def permutation(idx):
    if idx == N:
        print(perm)
        return
    for i in range(N):

        if not used[i]: # 이부분이 빽트레킹

            perm[idx] = arr[i]
            used[i] = 1 # 내가 i번 써부렷어
            permutation(idx + 1)
            used[i] = 0 # 다음인덱스 가기전에 0으로 초기화시켜주기

permutation(0)

