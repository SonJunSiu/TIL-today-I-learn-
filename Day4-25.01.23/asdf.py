# Blacklist
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 사용자 목록 예제 (아까 사용한 API 형식처럼 가정)
user_list = [
    {"name": "Leanne Graham", "company": "Romaguera-Crona"},
    {"name": "Ervin Howell", "company": "Deckow-Crist"},
    {"name": "Clementine Bauch", "company": "Romaguera-Jacobson"},
    {"name": "Patricia Lebsack", "company": "Keebler LLC"},
    {"name": "Chelsey Dietrich", "company": "Johns Group"},
    {"name": "Mrs. Dennis Schulist", "company": "Hoeger LLC"},
    {"name": "Kurtis Weissnat", "company": "Yost and Sons"},
    {"name": "Nicholas Runolfsdottir V", "company": "Abernathy Group"},
]

# censorship 함수: 블랙리스트 확인
def censorship(company_name, user_name):
    if company_name in black_list:  # 회사가 블랙리스트에 포함되어 있으면
        print(f"{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.")
        return False  # 블랙리스트일 경우 False 반환
    else:
        print(f"{company_name} 소속의 {user_name}: 이상 없습니다.")
        return True  # 블랙리스트가 아니면 True 반환

# create_user 함수: 사용자 목록을 딕셔너리로 생성
def create_user(user_list):
    censored_user_list = {}  # 회사 이름을 키로, 사용자 이름 리스트를 값으로 갖는 딕셔너리
    
    for user in user_list:
        company = user["company"]
        name = user["name"]
        
        # censorship 함수 호출
        if censorship(company, name):  # 회사가 블랙리스트에 없으면
            if company not in censored_user_list:
                censored_user_list[company] = []  # 회사 키 초기화
            censored_user_list[company].append(name)  # 사용자 이름 추가
    
    return censored_user_list

# 사용자 목록 처리
censored_user_list = create_user(user_list)

# 최종 결과 출력
print("\n검열 결과:")
print(censored_user_list)
