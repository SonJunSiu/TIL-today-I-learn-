'''
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int,input().split))) for _ in range(N)]

print(arr)

'''
   0 1 2 3
0  0 0 0 0
1  0 0 0 0
2  0 0 0 0
'''



arr1 = [[0] * 4 for _ in range(3)] #위에꺼 만드는법
    
for i in range(N) :
    for j in range(N) : 
        print(arr[i][j])   #i = 행 j = 열 안쪽은 행 바깥은 열  i 아래 j 오른쪽
'''
3 4
1 7 2 8
6 2 9 3
5 7 4 2
'''
s = 0
for i in range(N) :
    for j in range(M) :
        s += arr[i][j]  # 행, 열의 합 구하기

#열 우선 순회
for j in range(m) :
    for i in range(n) :
        f(array[i][j])

#지그재그 순회

for i in range(n):
    for j in range(m) :
        f(arra[i][j + (m-1 -2 * j) * (i % 2)])

# 델 타     매우중요!!
