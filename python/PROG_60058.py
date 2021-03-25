def balance(s):
    left, right = 0,0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        else :
            right+=1
    return left==right

def correct(s):
    stack = []
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else :
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    else: 
        return False


def solution(p):
    if correct(p): return p
    if len(p)==0: return p
    for index in range(2,len(p)+1,2):
        u = p[0:index]
        v = p[index:]
        if(not balance(u)): continue
        if(correct(u)): 
            u+=solution(v)
            break
        else:
            tmpstr="("
            tmpstr+=solution(v)
            tmpstr+=")"
            for i in range(1,len(u)-1):
                if u[i]=='(': tmpstr+=')'
                else: tmpstr+='('
            return tmpstr

    return u

p = input()
print(solution(p))