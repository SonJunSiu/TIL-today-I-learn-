T = int(input())

for i in range(T) :
    N = int(input()) # 카드의 수
    card = int(input()) # 카드에 적힌 숫자
    count = [0] * 10 #길이가 10리스트 0으로 초기화 0~9
    
    for j in range(N) :
        count[card % 10] += 1 # 나눈 숫자 자리에 +1 씩 증가
        card //= 10 # 몫만 남기고 버려요요
    
    max_count = 0 # 등장 횟수
    max_number = 0 # 카드 번호호

#count 리스트 중 가장 많이 나오는거 찾기 근데 그중에 가장 큰 값

    for num in range(10):  # 0부터 9까지 확인
        if count[num] > max_count:  #숫자 등장한 횟수 > 최빈값 등장 횟수 현재 숫자가 여태 숫자보다 더 많이 나온다
            max_count = count[num]  # 현재 숫자가 최빈값
            max_number = num # max_number를 현재 숫자로 업댓

        elif count[num] == max_count:  # 만약 새로운 숫자가 기존 값과 같은 횟수 ( 최빈값 여러개)
            if num > max_number:  # 숫자가 더 크면 갱신
                max_number = num 

    print(f'#{i + 1} {max_number} {max_count}') 
