# def updown(name):
#     answer = 0
#     for n in name:
#         if ord(n) == ord('Z'):
#             answer += 1
#         elif ord(n) > ord("L") and ord(n) != ord('Z'):
#             answer += 1
#             answer += (ord('Z') - (ord(n)))
#         else:
#             answer +=((ord(n)) - ord('A'))
#     return answer

# def left(name):
#     n = (len(name)//2) 
#     if 'A' in name[n:]:
#         return (len(name) - (name.count('A'))-1)
#     else:
#         return (len(name) - 1)

# def solution(name):
#     print(updown(name))
#     print(left(name))
#     answer=updown(name) + left(name)
#     return answer

#코드 발췌 : https://jgrammer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1

def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name] #가장 작은 경우의 수를 넣기
    idx, answer = 0, 0 
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0: #문자의 하나씩 돌면서 확인하고, 확인했으면 0으로 만들기 
            break
        left, right = 1, 1
        while make_name[idx - left] ==0: #0이면 계속 돌아라. 최솟값을 찾는 것이므로 작을수록 좋겠지
            left +=1
        while make_name[idx + right] ==0: #마찬가지로 0이면 계속 옆으로 가라
            right +=1
        answer += left if left < right else right #더 작은 값을 더하고
        idx += -left if left < right else right #만약 왼쪽으로 가는 게 더 작으면 빼야 하고, 그게 아니라면 index를 더해야 함
    return answer
