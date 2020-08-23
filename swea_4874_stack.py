T=int(input())
for test_case in range(1,T+1):
    stk = []
    cal = list(input().split())
    flag =0
    for c in (cal[:-1]):
        if c.isdigit():
            stk.append(c)
        else:
            try:
                a,b=int(stk.pop()),int(stk.pop())
                if c == "+":
                    result = a+b
                elif c == "-":
                    result = b-a
                elif c == "*":
                    result = a*b
                elif c == "/":
                    result = b/a
                stk.append(result)
            except:
                flag =-1
    if flag==-1 or len(stk)>1:
        print(f'#{test_case} error')
    elif flag == 0 and len(stk)==1: 
        print("#%s %d"%(test_case,int(stk[0])))
