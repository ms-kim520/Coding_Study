def solution(n,a,b):
    answer = 1
    while 1:
        q_a,r_a = divmod(a,2)
        q_b,r_b=divmod(b,2)
        a = q_a + r_a
        b = q_b + r_b
        if a == b:
            return answer
        else:
            answer+= 1
