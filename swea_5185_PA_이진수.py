conversion = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}
def binary(num):
    global result
    for i in range(4):
        mok = num // 2
        nam = num % 2
        result = str(nam) + result
        num = mok
    return 

T=int(input())
for test_case in range(1,T+1):
    N,String = map(str,input().split())
    final_result = ''
    for idx in String:
        result =''
        binary(conversion[idx])
        final_result+=result
    print(f'#{test_case} {final_result}')
