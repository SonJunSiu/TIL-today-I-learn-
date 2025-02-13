def solve(arr) :
    stack = [None] * len(arr) # 스택 선언?
    top = -1

    for i in arr :
        if top == -1 : # 아무 스택도 없다면
            top += 1
            stack[top] = i # 스택의 현재 top 위치에 요소 i 저장 이게 그 push

        else :
            if stack[top] == i : # top에 있는 요소가 현재 요소 i와 같다면
                top -= 1 # 스택에서 제거
            else:  # 반복문자 없을 때
                top += 1
                stack[top] = i

    return top + 1 # 스택의 문자 개수를 반환해야하니까


T = int(input())
for tc in range(T):
    arr = input()
    print(f'#{tc+1} {solve(arr)}')

