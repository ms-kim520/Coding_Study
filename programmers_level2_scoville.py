# 시간초과된 내 풀이 : 간단하게 pop 함수를 사용하고, 내장함수 sort를 이용하려 함. 답은 맞췄지만, 효율성에서 틀림
def solution(scoville, K):
    answer = 0
    while True:
        scoville.sort()
        a = scoville.pop(0)
        if a >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        b = scoville.pop(0)
        c=a + (b*2)
        scoville.append(c)
        answer +=1
    return answer
    
 #효율성을 챙기는 모범답안 : heapq
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new = min1 + 2*(min2)
        heapq.heappush(scoville,new)
        answer += 1
    return answer
