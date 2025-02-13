txt = input()

top = -1
stack = [0] * 100

ans = 1 # 짝이 맞다고 가정
for x in txt:
    if x == '(': # 여는 괄호 push
        top += 1
        stack[top] = x
    elif x == ')': # 닫는 괄호인 경우
        if top == -1:  # 스택이 비어있으면
            ans = 0
            break # for x
        else :
            top -= 1
                    # 소괄호만 있으므로 비교 작업 생략
if top > -1: # 여는 괄호가 남아 있으면
    ans = 0

print(ans)