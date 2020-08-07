T=int(input())
def binary_search(end,want):
    end=end;start=0;cnt=0;mid=0 #start가 1이 아닌점
    while start<=end:
        # mid=int((1/2)*(start+end)) #반으로 나누는 방식이 다름
        mid=(start+end)//2
        if mid==want:
            break
        elif mid>want:
            end=mid
            cnt+=1
        else:
            start=mid
            cnt+=1
        
    return cnt


for test_case in range(1,T+1):
    r,A,B = map(int,input().split())
    a=binary_search(r,A)
    b=binary_search(r,B)
    if a > b:
        print("#%s %s" %(test_case,'B'))
    elif a < b:
        print("#%s %s" %(test_case,'A'))
    elif a==b:
        print("#%s %d" %(test_case,0))


# TC = int(input())

# for tc in range(1, TC + 1):
#     info = list(map(int, input().split()))

#     result = []
#     for j in range(2):
#         start = 1
#         end = info[0]
#         page = info[j+1]
#         cnt = 0

#         while start <= end:
#             mid = (start + end) // 2
#             if mid == page:
#                 break
#             elif mid < page:
#                 start = mid
#                 cnt += 1
#             else:
#                 end = mid
#                 cnt += 1

#         result.append(cnt)

#     if result[0] < result[1]:
#         print('#%s'%tc,'A')
#     elif result[0] == result[1]:
#         print('#%s'%tc,0)
#     else:
#         print('#%s'%tc,'B')