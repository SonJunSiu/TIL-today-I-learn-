# 선형 큐
queue = [None] * 10
# 삽입 위치와 삭제 위치가 달라서 변수 2개 필요
N = 10
front = rear = -1 # fornt 맨 앞 rear 맨뒤
# 삽입(enqueue) : rear 를 1 증가시키고 그 위치에 새로운 요소 삽입
# 삭제(dequeue) : front를 1증가시키고 그위치에 요소 반환
#         (진짜 삭제는 아니고 재사용 못하는 상황)

def enqueue(data):
    global rear
    if rear == N-1:
        print('큐가 빵빵이')
    rear += 1
    queue[rear] = data
    

def dequeue():
    global front
    if front == rear :
        print('큐가 텅텅이')
    else:    
        front += 1
        return queue[front]
# 선형 큐
# 큐가 비었는지 어떻게 확인?  front와 rear 가 같으면 비어있음
# 큐가 가득찬 경우는 rear가 배열의 마지막 요소를 가르키고 있으면


enqueue(5)
enqueue(4)
enqueue(3)
enqueue(2)
enqueue(1)

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
