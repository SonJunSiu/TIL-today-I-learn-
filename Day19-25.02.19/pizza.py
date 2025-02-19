t = int(input())
 
for tc in range(1,t+1):
    n,m = map(int,input().split()) #N이 화덕수 M 피자수
    input_lst = list(map(int,input().split())) #치즈 수 
    pizza_lst = [el for el in enumerate(input_lst,start=1)]
    queue = [] #화덕    
     
    #    pizza_lst = [el for el in enumerate(input_lst)] 이걸로 안할거면 밑에껄로 작성
    # pizza_lst = []
    #
    # for i in range(m):
    #     input_lst[i] #input_lst[i] :치즈 양, i+1 = 피자번호
    #     pizza_lst.append((i+1,input_lst[i]))
 
    for i in range(n): #화덕의 크기만큼 피자 넣기
        queue.append(pizza_lst[i])
         
    #문제 조건에 따라서 n개의 피자가 화덕에 들어가야함.
    #다음에 들어갈 피자는 n번 피자
    next = n 
     
    while len(queue) > 1:  #피자가 하나 남을때까지 화덕 가동시키기.
        num,cheese = queue.pop(0)
        cheese = cheese//2
         
        if cheese == 0: #치즈가 다 녹음 : 얘는 빼고 새로운 피자 넣기
            #if 남아있는 피가자 있으면 넣기
            if next < m : #피자가 남아있다면
                queue.append(pizza_lst[next])
                next +=1
         
        else: #치즈 덜 녹음
            queue.append((num,cheese))
             
    last_pizza = queue.pop(0)
    print(f'#{tc} {last_pizza[0]}')



    

    