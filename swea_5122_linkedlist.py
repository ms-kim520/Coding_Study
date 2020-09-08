T=int(input())
for test_case in range(1,T+1):
    N,M,L = map(int,input().split())
    #N=수열의 길이, M = 추가횟수, L = 인덱스 번호
    lst = list(map(int,input().split()))
    for _ in range(M):
        info = list(input().split())
        character = info.pop(0)
        info = list(map(int,info))
        idx=info[0]
        if character == "I":
            a= [info[1]]
            lst[idx:idx] = a
        elif character == "D":
            lst.pop(idx)
        elif character == "C":
            lst[idx] = info[1]
    if L<len(lst):
        print(f'#{test_case} {lst[L]}')
    else:
        print(f'#{test_case} -1')
