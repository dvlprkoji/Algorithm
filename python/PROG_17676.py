pushTime = []
popTime = []

def minusTime(d, t, l):
    res = ""
    day=int(d)
    listStr = list(map(float,t.replace(':',' ').split()))
    Len = float(l.replace('s','').replace('',''))-0.001
    if listStr[2]<Len:
        listStr[2]+=60
        listStr[2]-=Len
        if listStr[1]<1:
            listStr[1] = 59
            listStr[0] -= 1
            if listStr[0]<0:
                listStr[0]+=60
                day-=1
        else: 
            listStr[1]-=1
    else: listStr[2]-=Len
    res+=str(day)
    for i in range(len(listStr)-1):
        if listStr[i]==0.0: res+="00"
        elif listStr[i]<10 : 
            res+="0"
            res+=str(int(listStr[i]))
        else: res+=str(int(listStr[i]))
    val = str(int(listStr[2]*1000))
    for i in range(5-len(val)): res+="0"
    res+=val
    return res

def countMax(t):
    s=set()
    day = t[0:2]
    to = ""
    to += t[2:4]
    to += " "
    to += t[4:6]
    to += " "
    to += t[6:8]
    to += "."
    to += t[8:]
    st = minusTime(day, to, '0.999s')
    en = minusTime(day, to, '0s')
    for i in range(len(popTime)):
        if int(pushTime[i])>int(en): continue
        if int(popTime[i])<int(st): continue
        s.add(i)
    return len(s)


def solution(lines):
    answer = 0

    for line in lines:
        pushTime.append(minusTime(15,line.split()[1],line.split()[2]))
        popTime.append(minusTime(15,line.split()[1],'0.001'))

    for t in range(len(pushTime)):
        answer = max(answer, countMax(pushTime[t]))
        answer = max(answer, countMax(popTime[t]))

    return answer

lines = [
"2016-09-15 00:00:00.000 3s"
]
print(solution(lines))