arr = [[0]*10 for _ in range(10)]

for r in range(10):
    for c in range(0, r + 1):

        if c == 0 or r == c:
            arr[r][c] = 1
        else:
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    
    for i in range(N):
        print(*arr[i[:i+1]])


# 정렬 거품 선택 카운팅 반복문으로 인덱스 조작 많이 연습하자