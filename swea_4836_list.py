T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    red =[]
    blue =[]
    for idx in range(N):
        x1,y1,x2,y2,color = (list(map(int, input().split())))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if color == 1:
                    red.append([i,j])
                else:
                    blue.append([i,j])
    new_list=[]
    for r in red:
        if r in blue:
            new_list.append(r)
    print('#%s %d'%(test_case,len(new_list)))
    