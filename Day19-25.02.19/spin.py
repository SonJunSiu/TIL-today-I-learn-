T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N 개의 숫자 배열 M번의 작업

    arr = list(map(int,input().split())) # 숫자배열
        
    for _ in range(M) : # M번의 작업동안
        ans = arr.pop(0) # ans라는 함수에 arr의 팝을 이어붙임
        arr.append(ans) # 다시 arr에 함

    print(f'#{tc} {arr[0]}')