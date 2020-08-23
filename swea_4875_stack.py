T=int(input())
#x=열, y=행


def check_in_maze(y,x):
    return (0<=y<N) and (0<=x<N) and (maze[y][x] == 0 or maze[y][x]==3) #0이거나 3인것만 반환


def escape_route(y,x):
    global answer
    if maze[y][x] == 3:
        answer = 1
        return answer
    visited.append((y,x))
 
    for i in range(4):
        new_x = start[0]+dir_x[i]
        new_y = start[1]+dir_y[i]
        if check_in_maze(new_y,new_x) and (new_y,new_x) not in visited:
            escape_route(new_y,new_x)


for test_case in range(1,T+1):
    answer = 0
    N=int(input())
    maze = []
    for n in range(N):
        line = list(map(int,input()))
        if 2 in line:
            start = [n,line.index(2)]
        maze.append(line)      

    visited =[]  

    dir_x = [-1,1,0,0]
    dir_y = [0,0,-1,1]

    escape_route(start[0],start[1])
    print(answer)


     