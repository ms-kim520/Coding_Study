def solution(files):
    import re
    file_lst = []
    for file_ in files:
        NUMBER=(re.findall('\d+',file_)[0])
        length_number= len(NUMBER)
        start=file_.index(NUMBER)
        end  = (length_number)+start - 1

        HEAD = file_[:start].lower() #알파벳의 크기가 상관이 없으므로 
        TAIL = (file_[end+1:])

        file_lst.append((HEAD,int(NUMBER),TAIL,file_))
    fileset = sorted(file_lst, key = lambda x: (x[0],x[1])) 
    # python sorted를 활용하면 key를 통해 어떻게 정렬할지 찾을 수 있음. 만약 원래 순서대로 두고 싶다면 key에 그 요소를 안 넣으면 됨
    return [''.join(x[3]) for x in fileset]
