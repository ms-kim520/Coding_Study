def solution(s):
    lst = s.split(' ')
    # print(lst)
    answer = []
    for l in lst:
        if l.isalpha() == False:
            answer.append(l)
        else:
            l=l.capitalize()
            answer.append(l)
    string = ' '.join(answer)
    return string
