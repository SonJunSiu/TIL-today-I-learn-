# 아래 함수를 수정하시오.
def even_elements(ele):
    odd_lsit=[]
    while ele :
        element = ele.pop(0)
        if element % 2 == 0 :
            odd_lsit.extend([element])
    return odd_lsit


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
