# 정렬 하려는 대상 배열
data = [7, 5, 3, 2, 1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 7]
N = len(data)
max_val = 7
# 정령 대상의 각 요소가 몇개씩 있는지 표시하는 배열
counts = [0] * max_val + 1
# 개수세기
for i in range(N) :
    # data[i]의 값이 몇개 나오는가?
    counts[data[i]] += 1 # 데이터의 i번째 인덱스에 +1해주는것
# 누적합 구하기 : 누적합을 구하면 각요소가 어디에 들어가는지 알 수 있다.
# 0번빼고, 1번부터 끝까지 앞에거랑 내거랑 더해서 내자리에 넣기
for i in range(1, len(counts)) :
    counts[i] += counts[i -1] #내 앞이랑 나랑 더해서 내자리에 넣는다.
# 정렬된 값이 들어갈 배열
sorted_arr = [0] * N
for i in range (N) :
    # data[i] 가 들어갈 위치를 찾아서 넣어주기
    # 들어갈 위치는 counts가 가지고 있다
    counts[data[i]] -= 1
    sorted_arr[counts[data[i]]] = data[i]

print(sorted_arr)