T=int(input())
for test_case in range(1,T+1):
    N,H,L = map(int,input().split())
    tree = [0]*(N+1)
    for _ in range(H):
        idx, value = map(int,input().split())
        tree[idx] = value
    num = N
    while num > 0:
        tree[num//2] += tree[num]
        num-=1
    print(f'#{test_case} {tree[L]}')
