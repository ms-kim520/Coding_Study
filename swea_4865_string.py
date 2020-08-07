T=int(input())
for test_case in range(1,T+1):
    find = list(input())
    string = list(input())
    find=set(find)
    c={}
    for f in find:
        c[f]=string.count(f)
    print("#%s %d" %(test_case,max(c.values())))