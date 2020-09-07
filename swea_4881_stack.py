# 참고 : https://tothefullest08.github.io/algorithm/2019/03/08/2_4881_min_sum/
# 주석만 첨가하였다

def findmin(row):
    global sum_value, min_value
    if sum_value > min_value:
        return #해봤자 소용없으므로
    if row == N : #한바퀴 돌았다면
        if sum_value < min_value: #최솟값보다 작다면 바꿔줘야지!
            min_value=sum_value
            return
    for col in range(N): #제시된 행의 개수만큼 돌아야 함
         if not visited[col]:
            visited[col] = True #지금 지나가므로 True로 해주기
            sum_value += array[row][col] #더해주기
            findmin(row+1) #그 다음 행으로 넘어가서 돌기 N이 될 때까지 
            #혹은 min값보다 훨씬 더 커서 더이상 돌지 않아도 될 때까지
            sum_value -= array[row][col] #빼기, 이제 그 다음 col로 넘어가야 하니까
            visited[col] = False

T=int(input())
for test_case in range(1,T+1):
    N=int(input()) #배열은 N*N크기이다
    array = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    # sum_lst = []
    sum_value, min_value = 0, (N * 9) #가장 최댓값을 정해놓기 (모든 값이 9일경우가 가장 크기 때문에)
    findmin(0)
    print('#{} {}'.format(test_case, min_value))
    
