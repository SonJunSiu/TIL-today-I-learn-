# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 인큐
rear += 1      # enqueue 1
queue[rear] = 1

rear += 1      # enqueue 2
queue[rear] = 2

rear += 1      # enqueue 3
queue[rear] = 3

while front != rear:
    front += 1
    t = queue[front]
    print(t)

    front += 1               # dequeue
    print(queue[front])
    front += 1               # dequeue
    print(queue[front])
# 그라나 빠다노 치즈 파슬리 밀가루 로즈마리 파스타면 생닭 레몬 버터 계란 당근 감자 관찰레 로스트팟..?




q = []
q.append(1)
