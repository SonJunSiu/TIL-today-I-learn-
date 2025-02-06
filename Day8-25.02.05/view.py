for i in range(1, 11) :
    result = 0 #총합 저장
    n = int(input()) #건물의 수
    h = list(map(int,input().split())) # 건물 높이
    for j in range(2, n-2) : # 2~n-3 까지 반복 앞뒤 2칸은 빼야하니까 j는 현재 검사하는 '건물'위치
        a1 = h[j] - h[j-2] #기준 건물에서 -2칸 그리고 기준건물 높이 -높이이
        a2 = h[j] - h[j-1] # -1
        a3 = h[j] - h[j+1] # +1
        a4 = h[j] - h[j+2] # +2
        if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 : # 좌 우 4칸 다 비어야 통과 기준건물에서 좌우 2건물 빼고 + 되야 오케이
            result += min(a1, a2, a3, a4) # 기준 건물이니까 min 사용 가능
    print(f'#{i} {result}')



# # 강사님 코드
# for tc in range(1, 11):
#     N = int(input())
#     data = list(map(int,input().split()))
#     reseult = 0
#     for i in range(2, N-2) : 
#         # 조망권 계산해서 result에 더하기
#         # 거리 2이내에 
#         #     
#     for j in range(i-2, i+3) :
#         if j == i : continue
#         if max_vv < data[j] :
#             max_vv = data[j]


#     # max_v : 주변 건물 중 최고 높이
#     # 만약 현재 건물 높이가 max_v보다 높다면 조망권 세대가 있다
#     # 그러니까 result에다 더해주기

#     if data[i] > max_vv:
#         result += data[i] - max_vv
    
#     print(f'#{tc} {result})