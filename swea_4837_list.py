T=int(input())
A=[1,2,3,4,5,6,7,8,9,10,11,12]
#멱집합 만드는 방법 고민하기
def powerset(s):
    masks = [ 1 << i for i in range(len(s)) ]
    for i in range( 1 << len(s) ):
        yield [ss for ss,mask in zip(s,masks) if mask & i ]
        
for test_case in range(1,T+1):
    N,K= map(int,input().split())
    hap =[]
    answer=0
for power in powerset(A):
    if len(power)==N and sum(power)==K:
        hap.append(power)
print("#%s %d"%(test_case,len(hap)))