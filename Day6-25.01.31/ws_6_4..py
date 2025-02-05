# 아래 함수를 수정하시오.
def get_keys_from_dict(dicts):
    return list(dicts)


# 최상위 딕셔너리와 하위 딕셔너리의 키를 추출하여 리스트로 반환해야함
def get_all_keys_from_dict(all):
    key = []
    for key in 



my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']




# ['name', 'age']
# ['person', 'name', 'age', 'location']