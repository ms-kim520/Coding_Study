def solution(clothes):
    d = {}
    answer = 1
    for c in clothes:
        d[c[1]] = d.get(c[1],0)+1
    x = [v+1 for k,v in d.items()] 
    for j in range(len(x)):
        answer = answer*x[j]
    # if len(x) == 1:
    #     answer = x[0]
    # else:
    #     answer =x[0]+(x[1]*x[1])+x[0]
    #     for j in range(2,len(x)):
    #         answer = answer+(answer*x[j])+x[j]
    return answer-1
