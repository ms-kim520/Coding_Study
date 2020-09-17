T=int(input())
for test_case in range(1,T+1):
    N=float(input())
    idx = 1
    result =''
    while N>0:
        if idx > 13:
            break
        mok = N//(1/2**(idx))
        N=N%(1/2**(idx))
        result += str(int(mok))
        idx +=1

    if idx > 13:
        print(f'#{test_case} overflow')
        # print('overflow')
    else:
        print(f'#{test_case} {result}')
        # print(result)
