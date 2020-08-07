T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    b=list(map(int,input().split()))
    answer = []
    while len(answer) < N:
        answer.append(max(b))
        del b[b.index(max(b))]
        answer.append(min(b))
        del b[b.index(min(b))]
    answer = answer[:10]
    answer=[str(x) for x in answer]
    lst = ' '.join(answer)
    print("#%s %s"%(test_case, lst))