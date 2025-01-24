data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
#아래에 코드를 작성하시오.

result = ('')
for i in data_1 :
    if i.isupper() or i == ' ' :
        result += i
print(result)




print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

for l in '내힘들다' :
    index = data_2.find(l)
    if index != -1 :
        arr.append(index)

print(arr)
arr.sort()
print(arr)

result2 = ''

# 무작위 한글이 작성된 문자열 data_2와 빈 리스트 arr이 주어진다. 
# data_2에서 문자열 '내힘들다'의 각 글자들이 위치한 index 번호를 find 메서드를 활용하여 찾는다. 
# 찾아낸 index번호를 리스트 arr에 append메서드로 추가한다.
#  arr을 출력한다. 
# sort 메서드를 활용해 arr 리스트를 오름차순 정렬한다. 
# 정렬된 arr을 출력한다. 
# data_2에서 정렬된 arr을 순회하여 얻은 각 요소 번째에 위치한 문자열을 출력한다. 
# 모든 문자열은 한 줄에 출력되어야 한다.

for str in arr :
    result2 += data_2[str]

print(result2)