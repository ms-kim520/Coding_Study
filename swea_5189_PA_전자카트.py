def DFS(y,x):
    global result,sub_result,visited_col
    if result < sub_result:
        return

    if y == N-1:
        result = sub_result
        return

    if y == x or x in visited_col:
        print(y,x,result)
        x+=1
        
        DFS(y,x)
    if x not in visited_col:
        visited_col.append(x)
        sub_result += office[y][x]
        y+=1
        print(y,x,result)
        DFS(y,0)
        visited_col.remove(x)
        sub_result -= office[y][x]


        
T=int(input())
for test_case in range(1,T+1):
    N = int(input())
    office = [list(map(int,input().split())) for _ in range(N)]
    visited_col = []
    result,sub_result = 987654321,0
    DFS(0,0)
    print(f'#{test_case} {(sub_result)}')
    
