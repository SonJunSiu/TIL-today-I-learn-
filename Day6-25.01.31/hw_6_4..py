def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()  
    new_dict[key] = value  
    return new_dict 

# 예제 실행
my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result) 
