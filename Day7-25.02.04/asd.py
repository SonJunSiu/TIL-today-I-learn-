# 학생 정보가 담긴 리스트
students = [
    {'name': '김싸피', 'score': 100, 'school': 'gumi'},
    {'name': '김싸피', 'score': 100, 'school': 'seoul'},
    {'name': '김싸피', 'score': 100, 'school': 'seoul'},
    {'name': '김싸피', 'score': 100, 'school': 'gumi'},
]

# (1) 학생들의 이름을 추출
names = []  # 이름을 저장할 빈 리스트 생성
for student in students:
    names.append(student['name'])
print("학생 이름들:", names)

# (2) 학생들의 총 점수를 계산
total_score = 0  # 점수 누적을 위한 변수
for student in students:
    total_score += student['score']
print("총 점수:", total_score)

# (3) 'gumi' 지역의 학생들을 추출
gumi_students = []  # 'gumi' 지역 학생 정보를 저장할 리스트
for student in students:
    if student['school'] == 'gumi':
        gumi_students.append(student)
    
print("'gumi' 지역 학생들:", gumi_students)

# (4) 리스트 슬라이싱: 처음 2명의 학생 정보를 추출
first_two = students[::-1]
print("처음 두 명의 학생 정보:", first_two)
