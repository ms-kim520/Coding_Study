T=int(input())
for test_case in range(1,T+1):
    N = input()
    M=(input())
    n=len(N);m=len(M)
    hap = 0
    for i in range(m-n+1):
        if N==M[i:i+n]:
            hap+=1
    if hap > 0:
        print("#%s %d"%(test_case,1))
    else:
        print("#%s %d"%(test_case,0))