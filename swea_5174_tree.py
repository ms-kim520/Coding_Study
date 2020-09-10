def check(parent):
    global count
    child=graph.get(parent)
    if child is None:
        return 
    elif len(child)==2:
        a = child.pop(0)
        b = child.pop(0)
        count+=2
        check(a)
        check(b)
    else:
        a = child.pop(0)
        count+=1
        check(a)

T=int(input())
for test_case in range(1,T+1):
    E,N = map(int,input().split())
    #E=간선의 개수 N=자식 노드의 수를 알아내야 하는 부모 노드
    lst = list(map(int,input().split()))
    graph = dict() 
    count = 1
    #딕셔너리로 트리 구조화
    for e in range(E):
        idx=e*2
        if lst[idx] in graph:
            graph[lst[idx]].append(lst[idx+1])
        else:
            graph[lst[idx]] = [lst[idx+1]]

    check(N)
    print(f'#{test_case} {count}')
