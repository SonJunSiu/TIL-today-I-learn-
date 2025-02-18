def solve(arr):
    stack = []
    for i in arr:
        if i not in '+-*/.':  # 숫자인 경우 스택에 넣기
            stack.append(int(i))

        elif i in '+-*/':  # 연산자인 경우 스택에서 두 개 꺼내기
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)  
                elif i == '*':
                    stack.append(a * b)  
                elif i == '/':
                    if b != 0:  
                        stack.append(a // b)
                    else:
                        return 'error'
            else:
                return 'error'
            
        elif i == '.':  # 결과 출력
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
    
    return 'error'  # `.`이 없을 경우

T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())
    print(f'#{tc} {solve(arr)}')
