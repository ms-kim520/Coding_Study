def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)

def solution(w,h):
    a=gcd(w,h)
    return (w*h)-(((w/a)+((h/a)-1))*a)
