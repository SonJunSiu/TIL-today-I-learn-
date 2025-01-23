# Blacklist
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 사용자 목록 예제
user_list = [
    {"name": "Ervin Howell", "company": "Deckow-Crist"},
    {"name": "Clementine Bauch", "company": "Romaguera-Jacobson"},
    {"name": "Chelsey Dietrich", "company": "Keebler LLC"},
    {"name": "Mrs. Dennis Schulist", "company": "Considine-Lockman"},
    {"name": "Kurtis Weissnat", "company": "Johns Group"},
    {"name": "Clementina DuBuque", "company": "Hoeger LLC"},
]

def censorship(company_name, user_name):
    if company_name in black_list: 
        print(f"{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.")
        return False  # 블랙리스트일 경우 False 반환
    else:
        print("이상 없습니다.")  
        return True  # 블랙리스트가 아니면 True 반환


def create_user(user_list):
    censored_user_list = {}  # 회사 이름을 키로, 사용자 이름 리스트 값
    
    for user in user_list:
        company = user["company"]
        name = user["name"]
        
        if censorship(company, name):  # 회사가 블랙리스트에 없으면
            if company not in censored_user_list:
                censored_user_list[company] = []  
            censored_user_list[company].append(name) 
    
    return censored_user_list

censored_user_list = create_user(user_list)


print(censored_user_list)
