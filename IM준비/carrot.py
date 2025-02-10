def solve_carrot_distribution():
    # 총 수확 횟수를 입력받습니다.
    T = int(input())
    
    # 결과를 저장할 리스트를 초기화합니다.
    results = []
    
    # 각 테스트 케이스에 대해 반복합니다.
    for case_number in range(T):
        # 당근의 개수를 입력받습니다.
        N = int(input())
        
        # 당근의 크기를 입력받아 리스트로 변환합니다.
        carrots = list(map(int, input().split()))
        
        # 당근의 크기를 오름차순으로 정렬합니다.
        carrots.sort()
        
        # 각 상자에 들어갈 수 있는 최대 당근 수는 N을 2로 나눈 몫입니다.
        max_per_box = N // 2
        
        # 최소 차이를 무한대로 초기화합니다.
        min_difference = float('inf')
        
        # 유효한 분배가 발견되었는지를 추적하는 변수입니다.
        found_valid_distribution = False
        
        # 첫 번째 상자의 크기를 1부터 N-2까지 시도합니다.
        for i in range(1, N - 1):
            # 두 번째 상자의 크기를 i+1부터 N-1까지 시도합니다.
            for j in range(i + 1, N):
                # 각 상자의 크기를 계산합니다.
                size1 = i
                size2 = j - i
                size3 = N - j
                
                # 각 상자의 크기가 0보다 크고, 최대 허용 크기보다 작거나 같은지 확인합니다.
                if size1 > 0 and size2 > 0 and size3 > 0 and size1 <= max_per_box and size2 <= max_per_box and size3 <= max_per_box:
                    # 유효한 분배가 발견되었음을 표시합니다.
                    found_valid_distribution = True
                    
                    # 세 상자 중 가장 큰 크기와 가장 작은 크기를 찾습니다.
                    max_size = size1
                    if size2 > max_size:
                        max_size = size2
                    if size3 > max_size:
                        max_size = size3
                    
                    min_size = size1
                    if size2 < min_size:
                        min_size = size2
                    if size3 < min_size:
                        min_size = size3
                    
                    # 최대 크기와 최소 크기의 차이를 계산합니다.
                    difference = max_size - min_size
                    
                    # 현재까지의 최소 차이를 갱신합니다.
                    if difference < min_difference:
                        min_difference = difference
        
        # 유효한 분배가 발견되었으면 최소 차이를 결과에 추가하고, 아니면 -1을 추가합니다.
        if found_valid_distribution:
            results.append(min_difference)
        else:
            results.append(-1)
    
    # 각 테스트 케이스에 대한 결과를 출력합니다.
    for case_number in range(T):
        print(f"#{case_number + 1} {results[case_number]}")

# 함수를 실행합니다.
solve_carrot_distribution()