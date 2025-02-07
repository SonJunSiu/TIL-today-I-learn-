T = int(input())

for tc in range(T) :
    N = int(input()) # 첫 줄에 칠할 영역의 개수 ( 네모 몇개 있느냐)
    space = [[0] * 10 for _ in range(10)]
    purple = 0 # 10*10 타일생성

    for _ in range(N) :
        r1, c1, r2, c2, color = map(int,input().split()) # 색칠 영역의 크기 # r1,2 c1,2 묶어야할듯

        for r in range(r1, r2+1) : # 색칠하는 행
            for c in range(c1, c2+1) : # 색칠하는 열
                if space[r][c] == 0 : # 아직 행열이 0이라면
                    space[r][c] = color # 색칠하기

                elif space[r][c] != color : # 만약 색이 겹친다면? 빨강은 1 파랑은 2 1+2는 뭐야? 3이야;;;
                    space[r][c] = 3
                    purple += 1 # 카운트1씩해줘

    print(f'#{tc+1} {purple}')




