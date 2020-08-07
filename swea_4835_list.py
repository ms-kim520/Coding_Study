T=int(input())
for test_case in range(1,T+1):
    # N,M=input().split()
    # N=int(N); M=int(M)
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    # a=input().split(' ')
    # a=[int(i) for i in a]
    #M개만큼 묶어서 더하기
    num_list =[]
    for i in range(0,N-M+1):
        num_list.append(sum(a[i:i+M]))
    # print('#'+str(test_case)+" "+str(max(num_list)-min(num_list)))
    print('#%s %d'%(test_case,max(num_list)-min(num_list)))