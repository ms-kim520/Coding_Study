T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # card= int(input())
    card =  list(map(int,list(input())))
    un=set(card)
    c = {}
    for u in un:
        c[u]=card.count(u)
    highest = max(c.values())
    
    high = []
    for v in c.items():
        if v[1] ==highest:
            high.append(v[0])
    print('#%s %d %d'%(test_case,max(high), highest))
    