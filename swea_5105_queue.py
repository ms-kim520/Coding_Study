#지금 확인하는 좌표가 범위안에 있는가? 0인가? 3인가?
def check(x,y):
    return 0<=x<N and 0<=y<N and (maze[x][y] == 0 or maze[x][y]==3)       


T=int(input())
pos_x = [0,0,-1,1]
pos_y = [-1,1,0,0]


def bfs(x,y):
    global answer
    Q.append((x,y))
    visited.append((x, y))
    while Q: 
        x,y=Q.pop(0)
        for idx in range(4):
            new_x = x + pos_x[idx]
            new_y = y + pos_y[idx]
            if check(new_x,new_y) and ((new_x, new_y) not in visited):
                Q.append((new_x,new_y))
                visited.append((new_x, new_y))
                distance[new_x][new_y] = distance[x][y] + 1
                if maze[new_x][new_y] ==3:
                    answer=distance[new_x][new_y] - 1
                    return answer


for test_case in range(1,T+1):
    N=int(input())
    # maze = [list(map(int,input().split())) for _ in range(N)]
    maze = []
    for n in range(N):
        row = list(map(int,input()))
        if 2 in row:
            start = [n,row.index(2)]
        maze.append(row)
    visited = []
    Q=[]
    distance = [[0]*N for _ in range(N)]
    answer = 0
    bfs(start[0],start[1])
    print(f'#{test_case} {answer}')