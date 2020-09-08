T=int(input())
for test_case in range(1,T+1):
    N,M,K = map(int,input().split())
    lst = list(map(int,input().split()))
    start = N
    if start >= (len(lst)):
        start=start%len(lst)
    for k in range(K):
        in_idx = start+M
        if in_idx == len(lst):
            temp = [lst[-1] + lst[0]]
            lst.extend(temp)
            start = in_idx
            continue
        elif in_idx > len(lst):
            in_idx = in_idx%(len(lst))
        temp = [lst[in_idx-1] + lst[in_idx]]
        lst[in_idx:in_idx] = temp
        start = in_idx 
    lst.reverse()
    print("#{0} {1}".format(test_case,(' '.join(str(x) for x in lst[:10]))))
