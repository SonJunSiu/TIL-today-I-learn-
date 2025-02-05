def ordered_difference_sets(set1, set2):
    A = set1 - set2
    B = set2 - set1

    if len(A) == len(B) :
        return (A, B)
    if len(A) < len(B) : 
        return(A, B)
    else :
        return(B, A)

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
