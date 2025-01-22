food_list = [
    {'종류': '한식', '이름': '잡채'},
    {'종류': '채소', '이름': '토마토'},
    {'종류': '중식', '이름': '자장면'},
]

for food in food_list:
    # 조건에 따라 종류를 변경하거나 메시지 출력
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    print(f"{food['이름']} 은/는 {food['종류']} (이)다.")
    
    if food['이름'] == '자장면':
        print("자장면엔 고춧가루지")

# 반복문 종료 후 food_list 출력
print("\nfood_list:", food_list)
