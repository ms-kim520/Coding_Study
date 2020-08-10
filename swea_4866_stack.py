T=int(input())
for test_case in range(1,T+1):
    bracket = list(input())
    check= []
    flag =True
    for idx,b in enumerate(bracket):
        if b=="{" or b == "(":
            check.append(b)
        elif b == "}" or b == ")":
            if len(check)==0:
                flag =False
                break
            else:
                c = check.pop()
                if c == '(' and b != ")":
                    flag=False
                    break
                elif c == '{' and b!='}':
                    flag=False
                    break
        
    if flag and len(check)==0:
        print("#%s %d" %(test_case,1))
    else:
        print("#%s %d" %(test_case,0))
