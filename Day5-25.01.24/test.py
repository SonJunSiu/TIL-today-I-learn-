# 아래 함수를 수정하시오.
def find_min_max(number):
    return min(number), max(number)
    


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

# 주어진 리스트에서 최솟값과 최댓값을 찾는 find_min_max 함수를 작성하시오. 
# 리스트를 인자로 받아 최솟값과 최댓값을 튜플로 반환해야 한다