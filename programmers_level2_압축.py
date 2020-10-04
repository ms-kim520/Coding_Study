# 출처: https://geonlee.tistory.com/43 [빠리의 택시 운전사]
def solution(msg):
    # dictionary = ['A','B','C','D','E',"F",'G','H','I','J','K','L','M',"N",'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic = dict()
    lst = []
    [lst.append(chr(i)) for i in range(ord('A'),ord('Z')+1)]
    for idx,char in enumerate(lst):
        dic[char] = idx+1
    answer = []
    maxId = 26
    idx = 0
    length = 0 #문자열에 대한 길이
    # while idx < len(msg):
    while True:
        length += 1

        if not msg[idx:idx+length] in dic:
            answer.append(dic[msg[idx:idx+length-1]])
            maxId += 1
            dic[msg[idx:idx+length]] = maxId
            idx+=length-1
            length = 0
        else:
            #문제의 포인트는 사전에 없는 문자가 나올 때까지 length를 돌린다는 것. 그리고 그 length를 활용하여 다음 인덱스를 정하는 것
            if idx+length-1 == len(msg):
                answer.append(dic[msg[idx:idx+length-1]])
                break
    return answer

# 원래는 flag를 통해 사전에 추가된 문자열의 길이에 따라 그 위치를 반환하게 하려 했지만, 바로 다음 글자를 가지고 오지 못하고, flag에 종속되는 문제가 발생
        # if flag == 1:
        #     answer.append((dictionary.index(msg[idx]))+1)
        #     dictionary.append(msg[idx:idx+2])
        #     print(f'#{idx} : {msg[idx:idx+2]} & {dictionary[-1]}')
        #     flag+=1
        #     idx+=1

    #     elif flag>1:
    #         for f in range(flag,0,-1):
    #             if msg[idx:idx+f] not in dictionary:
    #                 print(f'{idx} : {msg[idx:idx+f]} not in dictionary')
    #                 dictionary.append(msg[idx:idx+f])
    #                 dictionary = list(dict.fromkeys(dictionary))
    #                 print(f'#{idx} & flag: {f} --> {msg[idx:idx+f]}')
    #                 flag = f
    #             elif msg[idx:idx+f] in dictionary:
    #                 print(f'{idx} : {msg[idx:idx+f]}  in dictionary')
    #                 answer.append((dictionary.index(msg[idx:idx+f]))+1)
    #                 dictionary.append(msg[idx:idx+f+1])
    #                 dictionary = list(dict.fromkeys(dictionary))
    #                 print(f'#{idx} & flag: {f} --> {msg[idx:idx+f]} & {(dictionary.index(msg[idx:idx+f]))+1}')
    #                 flag = f+1
    #                 idx+=f
    #                 break
    # # answer.append((dictionary.index(msg[-1]))+1)
    # return answer,dictionary
