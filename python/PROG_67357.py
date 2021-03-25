import itertools
import copy
def solution(expression):
    maxval = 0
    arr = []
    tmp = ""
    s = set()
    for i in range(len(expression)):
        if ord(expression[i])>=ord('0') and ord(expression[i])<=ord('9'):
            tmp+=expression[i]
        else:
            arr.append(tmp)
            arr.append(expression[i])
            tmp=""
            s.add(expression[i])
    arr.append(tmp)
    op = list(itertools.permutations(s,len(s)))
    for opcase in op:
        res = copy.deepcopy(arr)
        for operand in opcase:
            nextval = []
            while len(res)!=0 :
                val = res.pop(0)
                if val==operand:
                    if val=='*':
                        a = int(nextval.pop())
                        b = int(res.pop(0))
                        nextval.append(str(a*b))
                    elif val == '+':
                        a = int(nextval.pop())
                        b = int(res.pop(0))
                        nextval.append(str(a+b))
                    else :
                        a = int(nextval.pop())
                        b = int(res.pop(0))
                        nextval.append(str(a-b))
                else:
                    nextval.append(val)
            res = nextval
        maxval = max(maxval, abs(int(res[0])))
    return maxval