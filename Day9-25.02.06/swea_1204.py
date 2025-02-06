from collections import Counter

T = int(input())  # 테스트 케이스 개수

for _ in range(T):  # 여러 개의 테스트 케이스 처리
    G = int(input())  # 테스트 케이스 번호
    points = list(map(int, input().split()))  # 점수 리스트로 변환

    counter = Counter(points)  # 점수별 몇번 등장했는지 계산
    max_count = max(counter.values())  # 등장 횟수 중 가장 큰 값을 알려줌
   # (71X 71이 '3'번 나왔다는걸 알려줌)

    # 최빈값 중 가장 많은 값 찾기
    most_common_value = max([k for k, v in counter.items() if v == max_count])
    # counter.item() 는 (점수, 등장 횟수) 쌍을 리스트로 반환
    # k는 점수, v는 등장횟수 for k, v in counter.items() k,v하나씩 가져옴
    # if v == max_count 
    print(f"#{G} {most_common_value}")  
