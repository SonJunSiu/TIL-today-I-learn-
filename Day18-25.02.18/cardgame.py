def solve (A, B): # 조편성 어케하노
    if A == B :
        return A
    

def winner (A, B):
    if arr[A] == arr[B]:
        return A
    elif arr[A] == 1:   # 가위를 냈을때 
        if arr[B] == 2: # 가위 대 바위
            return B
        else :
            return A   # 가위 대 보
        
    elif arr[A] == 2 :  # 바위를 냈을때
        if arr[B] == 1: # 바위 대 가위
            return A 
        else :          # 바위 대 보
            return B
        
    else :              # 보자기를 낸 경우
        if arr[B] == 1 : # 보 대 가위는
            return B
        else :
            return A       # 보 대 바위
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = solve(A, B)
    print(f'#{tc} {result}')
