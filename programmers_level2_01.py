def to_binary(n):
    result = ''
    while n//2 != 0:
        mok = n%2
        n=n//2
        result+=str(mok)
    one = result.count('1')
    return one

def solution(n):
    answer = 0
    one =to_binary(n)
    next_one = 0
    next_n = n
    while next_one != one:
        next_n += 1
        next_one=to_binary(next_n)
    answer = next_n
    return answer
