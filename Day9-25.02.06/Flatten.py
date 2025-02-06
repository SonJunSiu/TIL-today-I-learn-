# 작업 중간에라도 가장 높은곳과 낮은곳의 차이가 1이하라면 종료
# 작업은 횟수 제한이 있으며 작업 후 최고점과 최저점의 차이를 반환해야한다


for tc in range (1, 11) : #테스트 케이스

    work = int(input()) #작업가능 횟수
    box = list(map(int,input().split())) #박스 높이

    # 최대 높이를 찾고 -1 최저 높이를 찾고 +1
    # 가로 세로의 높이는 100 이하
    for _ in range (work):

        top_box = 0
        bottom_box = 0
        for i in range (100) : # 상자 최고, 최저 높이 찾기
            if box[i] > box[top_box] :   # 현시점 가장 높은 박스가 있다면 top에 저장
                top_box = i
            if box[i] < box[bottom_box] :  # 현시점 가장 낮은 박스가 있다면 bottom에 저장
                bottom_box = i
        if box[top_box] - box[bottom_box] <= 1: # 최고 최저의 차이가 1이하라면 종료
            break

        box[top_box] -= 1
        box[bottom_box] += 1
        #작업 끝 내가 찾은 top,bottom은 인덱스임

        #근데 이제 작업이 끝나고 박스의 최고 높이 최저높이를 또 찾아야함 
        for i in range(100) :
            if box[i] > box[top_box] : # 현시점 가장 높은 박스를 top에 저장
                top_box = i
            if box[i] < box[bottom_box] :
                bottom_box = i

    print(f'#{tc} {box[top_box] - box[bottom_box]}') # 최고 - 최저
