def updown(name):
    answer = 0
    for n in name:
        if ord(n) == ord('Z'):
            answer += 1
        elif ord(n) > ord("L") and ord(n) != ord('Z'):
            answer += 1
            answer += (ord('Z') - (ord(n)))
        else:
            answer +=((ord(n)) - ord('A'))
    return answer

def left(name):
    n = (len(name)//2) 
    if 'A' in name[n:]:
        return (len(name) - (name.count('A'))-1)
    else:
        return (len(name) - 1)

def solution(name):
    print(updown(name))
    print(left(name))
    answer=updown(name) + left(name)
    return answer
