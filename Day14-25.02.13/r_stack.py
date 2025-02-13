# stack을 만들기 위해서 필요한 거
# 1. 리스트 : 데이터를 저장하는 목적
# 2. top 변수 : stack의 마지막 요소를 가리키는 변수
# 3. push, pop라는 동작을 해야함

class MyStack:   # class를 쓰는 이유가 뭐였지
    # 상태값 : 리스트. top
    def __init__(self, length):
        self.s = [None] * length # ...?
        self.top = -1 # 초기화 -1
    def push(self, data):
        self.top += 1
        self.s[self.top] = data

        pass

    def pop(self):
        value = self.s[self.top]   # 마지막 위치를 일단 value에 담다
        self.top -= 1
        return  value

stack = MyStack(10)
stack.push('sss')
stack.push('SS')
stack.push('SR')
stack.push('SL')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


# sjs3 = -1
# st2 = [0]*100

# sjs3 += 1
# st2[sjs3] = 'A'

# sjs2 = -1
# sjs2 += 1
# st1 = [0]*20
# st1[sjs2] = 'A'

# sjs1 = -1
# st3 = [0]*100

st1 = MyStack()
st2 = MyStack()
st3 = MyStack()
st1.push('A')


























def solution(arr):
    data = [None] * len(arr)  # 스택 선언
    top = -1

    for i in arr:
        if top == -1:  # 스택에 아무것도 없을 때
            # push
            top += 1
            data[top] = i
        else:
            if data[top] == i:  # 반복문자 있을 때
                # pop
                top -= 1
            else:  # 반복문자 없을 때
                # push
                top += 1
                data[top] = i

    # 남은 글자 개수: top+1
    ans = top + 1
    return ans


'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

'''

case = int(input())
for _ in range(case):
    arr = input()
    print(f'#{_ + 1} {solution(arr)}')
