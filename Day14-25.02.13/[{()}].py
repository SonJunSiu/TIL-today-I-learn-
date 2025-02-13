T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    stack = [0] * 100
    top = -1
     
    # 닫는 괄호가 먼저 등장하는 경우 방지 하기 위함
    ans = 1 # 짝이 맞는건 1
    for i in text :
        if i in '({' :  # 여는 괄호
            top += 1
            stack[top] = i

        elif i in ')}' : # 닫는 괄호
            if top == -1:
                ans = 0 # 짝이 맞지 않는건 0
                break

            if (i == ')' and stack[top] != '(') or (i == '}' and stack[top] != '{'): # ( ) {  }  괄호의 짝이 맞지 않는경우에는
                ans = 0
                break
            top -= 1

    if top >= 0:  # 스택에 여는 괄호가 남아있다면 짝이 맞지 않음
        ans = 0

    print(f'#{tc} {ans}')  # 결과 출력


