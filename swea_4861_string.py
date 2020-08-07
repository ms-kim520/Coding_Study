#정해진 길이(M)의 회문은 1개 존재한다
#가로로 search -> 세로로 search해야 할 듯
T=int(input())
#회문인지 아닌지 함수 선언
def is_Palindrome(s):
    return s==s[::-1] #거꾸로도 같은지 확인하는 함수

for test_case in range(1,T+1):
    N,M=map(int,input().split())
    Palindrome = [] #입력받을 문자열 
    for n in range(N):
        Palindrome.append(input()) #차례대로 입력받기
    for i in range(N): 
        s=''
        for j in range(N):
            s+=Palindrome[j][i]
        Palindrome.append(s) #세로줄도 차례대로 넣어주기
    
    for l in range(len(Palindrome)):
        for k in range(N-M+1): #N과 M이 다른 경우도 있을 수 있기 때문에 잘라주기
            if is_Palindrome(Palindrome[l][k:k+M]) == True:
                print("#%s %s"%(test_case,Palindrome[l][k:k+M]))