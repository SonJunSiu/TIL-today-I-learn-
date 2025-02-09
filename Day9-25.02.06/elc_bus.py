# K = 갈 수 있는 수
# N = 최종 목적지
# M = 충전기 있는 정류장 개수

# 총 10칸
# 3칸 갈수 있고
# 1 3 5 7 9 번에 충전기가 있어 


# 현위치 + K 안에 주유소가 있어야 한다 
# 만약 이 안에 없으면? 0
T = int(input())

for tc in range(1, T+1) :


    K, N, M = map(int,input().split()) 
    gs = list(map(int,input().split())) #  충전기 있는 정류장 번호

    end = [0] * N # 도착거리 만큼 만들어야지
    for i in gs :
        end[i] += 1 #충전기 있는 정류장 표시 있으면 1 없으면 0

    now = 0 # 현재위치
    charge = 0 # 충전 횟수

    while now + K < N : #현재장소+K 가 N보다 작을때 동안 이동
        
        charge_station = 0 # 초기화 해야함
        
        for i in range(now+1, now + 1 + K): # 현재 다음 장소부터 충전소를 찾아야 하니께 최대범위까지 i는 이동가능한 정류장 번호
            if i < N and end[i] == 1:
                charge_station = i  # N 종점까지 가는 동안, K 범위 안에 있는 충전소가 종점을 넘지 않고,
                                       # end 리스트에서 1(충전소 있음)인 곳 중에서 가장 먼 곳을 찾는다.    
        
        if charge_station == 0 : #충전소가 없다면
            charge = 0 #충전이 안되고
            break #버스가 멈춰요

        now = charge_station # 마지막 충전소에 들렸다면?
        charge += 1 #스택 +1 합니다

    print(f'#{tc} {charge}')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) 
    gs = list(map(int, input().split()))  # 충전소 위치 

    now = 0  # 현재 위치
    charge = 0  # 충전 횟수

    while now + K < N:  # 종점에 도착하기 전까지 반복
        charge_station = -1  # 이동 가능한 충전소 초기화

        # 현재 위치(now)에서 K 거리 내에서 가장 멀리 있는 충전소 찾기
        for station in gs:
            if station > now + K:  # 이동 가능한 거리(K) 초과하면 중단
                break
            charge_station = station  # 충전소가 존재하는 가장 먼 위치 저장

        if charge_station == -1 or charge_station == now:  # 이동 가능한 충전소가 없으면 종료
            charge = 0
            break

        now = charge_station  # 충전소로 이동
        charge += 1  # 충전 횟수 증가

    print(f'#{tc} {charge}')

