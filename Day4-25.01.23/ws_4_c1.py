matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.


matrix_len = len(matrix)
matrix_len = 0
for num in matrix :
    matrix_len += 1
print(matrix_len)

for number in matrix :
    temporary_len = 0
    for element in matrix :
        temporary_len += 1
    if temporary_len <= 4 :
        print(f'{number}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.') 

for number in range(len(matrix)) :
    for n in range(len(matrix[number])) :
        print(f'matrix의 {number},{n} 번째 요소의 값은 {matrix[number][n]}입니다.')    

       
       




