T = int(input())
for i in range(1, T+1) :
    N = int(input())
    A = list(map(int,input().split()))
    print(f'#{i} {max(A)-min(A)}')