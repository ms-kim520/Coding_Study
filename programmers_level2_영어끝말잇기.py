def solution(n, words):
    seen = []
    for idx, x in enumerate(words):
        if len(x) == 1:
            q,r=divmod(idx,n)
            return [r+1,q+1]
        
        if len(seen) >=1:
            if seen[-1][-1] != x[0]:
                q,r=divmod(idx,n)
                return [r+1,q+1]
            if x in seen:
                q,r=divmod(idx,n)
                return [r+1,q+1]
        seen.append(x)    
    return [0,0]
