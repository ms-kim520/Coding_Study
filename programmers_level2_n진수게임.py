#모든 진법으로 변환할 수 있는 코드
# 참고 : https://brownbears.tistory.com/468
NOTATION = '0123456789ABCDEF'

def notation_conversion(number,base):
    q,r = divmod(number,base) #number/base하여 몫과 나머지 출력
    n = NOTATION[r]
    return notation_conversion(q,base) + n if q else n #제어장치, q가 계속 있으면 고 그게 아니면 n하고 끝

def solution(base, t, m, p):
    number_length=t*m
    number_lst = []
    idx=0
    while len(number_lst) < number_length:
        number_lst.extend([x for x in notation_conversion(idx,base)])
        idx += 1
    number_lst=number_lst[:number_length]
    answer = ''
    for idx in range(p-1,number_length,m):
        answer += number_lst[idx] 
    return answer
