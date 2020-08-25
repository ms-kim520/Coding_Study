T=int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    cheese = list(map(int,input().split()))
    oven = cheese[:N]
    rest = cheese[N:]    
    Q1 = [i+1 for i in range(N)]
    Q2 = [N+1+i for i in range(M-N)]
    i = N -1
    idx = 0
    done = []
    while Q1.count(0)<N-1:
        idx = (i+1)%N
        oven[idx]=oven[idx]//2
        if oven[idx] == 0 and len(rest) != 0:
            oven[idx] = rest.pop(0)
            Q1[idx] = Q2.pop(0)
            i+=1
        elif oven[idx] == 0 and len(rest) == 0 and idx not in done:
            done.append(idx)
            Q1[idx] = 0
        elif oven[idx] == 0 and len(rest) == 0 and idx in done:
            i+=1
        else:
            i+=1
    print(f"#{test_case} {max(Q1)}")
