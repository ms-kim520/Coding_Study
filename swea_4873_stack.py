T=int(input())

for test_case in range(1,T+1):
    string_ =list(input())
    stk=[]
    for idx,s in enumerate(string_):
        if idx == 0 or len(stk)==0:
            stk.append(s)
        else:
            if stk[-1] == s:
                stk.append(s)
                del stk[-2:]
            else:
                stk.append(s)
    print("#%s %d"%(test_case,len(stk)))
