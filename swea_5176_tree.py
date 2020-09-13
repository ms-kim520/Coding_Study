#참고 사이트 : https://hongsj36.github.io/2020/01/27/IM_Tree/

def numbering(num):
    global lst,cnt
    if num <= N:
        numbering(num*2)
        lst[num] = cnt
        cnt+=1
        numbering(num*2 + 1)
def result():
    return ' '.join(map(str,(lst[1],lst[N//2])))


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    lst = [0]*(N+1)
    cnt = 1
    numbering(1)
    a=result()
    print(f'#{test_case} {a}')
