T= int(input())
for test_case in range(1,T+1):
    # N:리스트의 길이, M: 추가횟수 L : 출력할 인덱스 번호
    N,M,L = map(int,input().split())
    lst = list(map(int,input().split()))
    for m in range(M):
        idx,add = map(int,input().split())
        lst.append(add)
        for n in range(1,len(lst[idx:])):
            lst[n*-1] = lst[(n+1)*-1]
            # print(lst)
        lst[idx] = add
    print(f'#{test_case} {lst[L]}')




