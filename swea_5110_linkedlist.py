T=int(input())
#flag의 사용으로 더 쉽게 할 수 있음
for test_case in range(1,T+1):
    #N : 수열의 길이, M : 수열의 개수
    N,M = map(int,input().split())
    first = list(map(int,input().split()))
    for m in range(M-1):
        # print(first)   
        second = list(map(int,input().split())) 
        check = True
        for idx in range(len(first)):
            if first[idx] > second[0]:
                first[idx:idx] = second #이런 방식으로 집어넣을 수 있다...!
                check =False
            # if (second[0]<max(first)) and second[0]<first[idx]: #시간초과...
                # temp1 = first[idx:]
                # temp2 = first[:idx]
                # first = temp2 + second + temp1
                break
        if check:
            first.extend(second)
            # elif (second[0]>max(first)):
            #     first = first + second
    # first_temp = [first[x * (-1)] for x in range(1,11)]
    # print(first_temp)
    first.reverse()
    print("#{0} {1}".format(test_case,(' '.join(str(x) for x in first[:10]))))
# print(' '.join(str(x) for x in l))