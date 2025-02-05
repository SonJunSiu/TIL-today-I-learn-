matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
matrix_len = 0
for ele in matrix :
    matrix_len += 1
print(matrix_len)

for num in matrix :
    temporary_len = 0
    for elem in num :
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{num}리스트는{temporary_len}개 만큼')


for i in range (matrix_len):
    row = matrix[i]
    row_len = 0
    for _ in row :
        row_len += 1
    for y in range(row_len):
        print(f"matrix의 {i}, {y} 번째 요소의 값은 {matrix[i][y]} 입니다.")
