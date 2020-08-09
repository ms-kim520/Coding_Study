T=int(input())

def Paper(x):
    if x==10:
        return 1
    elif x == 20:
        return 3
    else:
        return Paper(x-10) + (Paper(x-20)*2)

for test_case in range(1,T+1):
    N=int(input())
    print('#%s %d'%(test_case,Paper(N)))

