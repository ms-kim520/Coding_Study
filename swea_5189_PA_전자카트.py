def move(y,x):
    global result
    if x == N:
        return
    else:
        result += office[y][x]
        y+=1
        if y>=N:
            y = y%N
        x+=1
        move(y,x)
        
T=int(input())
for test_case in range(1,T+1):
    N = int(input())
    office = [list(map(int,input().split())) for _ in range(N)]
    result_list = []
    x = 0
    for y in range(N):
        result = 0
        move(y,x)
        result_list.append(result)
    result_list.remove(0)
    print(f'#{test_case} {min(result_list)}')
    
