# start번부터 end번까지 학생중에 승자를 반환하는 함수
def solve (A, B): # 조편성 어케하노
    if A == B:
        return A
    mid = (A + B) // 2 
    # start~mid까지 승자 찾기 # mid+1 ~end까지 학생중 승자 찾기 
    win1 = solve(A, mid)

    winner2 = solve(mid+1, B)
        # 전체를 두개 그룹으로 나누기? 나눈걸 또 나누기?


    

def winner (A, B):
    if arr[A] == arr[B]: #비길경우에는 편의상
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
