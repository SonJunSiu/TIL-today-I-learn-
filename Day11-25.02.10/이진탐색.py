'''
def solve(P, Pa, Pb):   # P: 전체 쪽  Pa, Pb : 찾아야할 쪽
    A_start = 1  # A 시작하는 첫 쪽
    last_A = P # A 탐색 마지막

    B_start = 1   # B 시작 첫 쪽
    last_B = P # B 탐색 마지막

    while A_start <= last_A and B_start <= last_B :   # A,B 탐색 범위가 있을때만 진행
        mid_A = (A_start+ last_A) // 2 # A 중간 페이지
        mid_B = (B_start + last_B) // 2 # B 중간 페이지

        if mid_A == Pa and mid_B == Pb : # 둘 다 동시에 끝났을 경우
            return 0
        
        elif mid_A == Pa : # A가 먼저 마지막 목표 페이지를 찾았을경우
            return 'A'
        elif mid_B == Pb : # B가 먼저 마지막 목표 페이지 찾았을 경우
            return 'B'
        
        # 탐색 범위 다시 설정?
        if mid_A > Pa : # A의 중간값이 목표 페이지 보다 크다면 왼쪽으로 이동
            last_A = mid_A # 탐색 범위의 끝을 줄여서 왼쪽만 탐색

        else : # A의 중간값이 목표보다 작다면 오른쪽으로 이동
            A_start = mid_A

        if mid_B > Pb : # B의 중간값이 목표 보다 크다면 왼쪽으로 이동
            last_B = mid_B

        else : # B의 중간값이 목표보다 작다면 오른쪽으로 이동
            B_start = mid_B

T = int(input()) # 테스트 케이스 입력
for tc in range(1, T+1) :
    P, Pa, Pb = map(int, input().split())  # 전체 페이지 수, A와 B의 목표 페이지
    answer = solve(P, Pa, Pb) # solve 함수 호출
    print(f'#{tc} {answer}')
'''


        


