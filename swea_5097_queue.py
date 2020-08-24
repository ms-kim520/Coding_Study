T=int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    a = (M%N)
    # print(a)
    print(f"#{test_case} {lst[a]}")