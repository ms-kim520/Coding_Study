# #처음부터 확인하는 코드 -> 틀렷다고 나옴 어디에서 틀린 걸까?
# T=int(input())
# for test_case in range(1,T+1):
#     N=int(input())
#     lst = list(map(int,input().split()))
#     tree = [0]
#     tree.extend(lst)
#     num = 1
#     for _ in range(N//2):
#         if not tree[num]<=tree[num*2]:
#             a = tree[num]
#             tree[num] = tree[num*2]
#             tree[num*2] = a
        
#         if N+1>(num*2)+1 and not tree[num]<=tree[(num*2)+1]:
#             b = tree[num]
#             tree[num] = tree[(num*2)+1]
#             tree[(num*2)+1] = b
#         num+=1

#     last = []
#     while N > 0:
#         N=N//2
#         last.append(tree[N])
#     if len(last) > 0:
#         print(f'#{test_case} {sum(last)}')
#     else:
#         print(f'#{test_case} 0')


#뒤에서부터 확인하는 코드로 수정하기
def check(N):
    global tree
    if N >= 2:
        if tree[N]<tree[N//2]:
            tree[N], tree[N//2] = tree[N//2], tree[N]
            print(f'{N} : {tree}')
            check(N//2)


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst = list(map(int,input().split()))
    tree = [0]
    lot = len(tree) #length of tree
    for l in lst:
        tree.append(l)
        check(lot-1)
    print(tree)
