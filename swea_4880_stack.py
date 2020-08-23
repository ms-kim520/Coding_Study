
def tree(start,end):
    if start==end:
        return start
    else:
        first_value = tree(start,(start+end)//2)
        second_value = tree(((start+end)//2)+1,end)
        return win(first_value,second_value)

def win(x,y):
    if (card[x-1] == 1 and card[y-1]==1) or  (card[x-1] ==1 and  card[y-1]==3):
        return x
    elif (card[x-1] == 2 and  card[y-1]==2) or  (card[x-1] ==2 and  card[y-1]==1):
        return x
    elif (card[x-1] == 3 and  card[y-1]==3) or  (card[x-1] ==3 and  card[y-1]==2):
        return x
    return y


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    card = list(map(int, input().split()))
    start = 1
    end = N
    print(f'#{test_case} {tree(start,end)}')