# 아래 함수를 수정하시오.
def remove_duplicates(num):
    new_lst = []
    for n in num :
        if n not in new_lst :
            new_lst.append(n)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
