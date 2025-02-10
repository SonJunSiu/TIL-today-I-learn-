def seq_search(a, n, key) :
    for i in range(n):
        if a[i] == key:
            return i
    return -1
arr = [4, 9, 11, 23, 2, 19 ,7]

print(len(arr))
# print(seq_search(arr, len(arr), 4))

# arr = [[1,2,3],[4,5,6],[7,8,9]]

# N = 3
# key = 5
# ans = 0 #key가 있으면 1, 없으면 0
# for i in range(N) :
#     for j in range(N) :
#         if arr[i][j] == key:
#             ans = 1
#             break 


# def seq_search(a,n,key):
#     for i in range(n) :
#         if a[i] == key:
#             return i
#         elif a[i] > key :
#             return -1
#     return -1 # 모든 원소가 key보다 작으면
# arr = [4, 9, 11, 23, 2, 19 ,7]
# arr.sort()
# print(arr)
# print(seq_search(arr, len(arr), 11))
# print(seq_search(arr, len), 100)