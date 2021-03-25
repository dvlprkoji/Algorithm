def solution(s):
    minval = 1001
    for i in range(1,(len(s)//2)+1):
        data = ""
        sliceindex = 0
        datacount = 1
        exstr = s[sliceindex:sliceindex+i]
        sliceindex+=i
        while sliceindex+i<=len(s):
            if s[sliceindex:sliceindex+i] == exstr:
                datacount+=1
                sliceindex+=i
            else:
                if datacount==1:
                    data += exstr
                    exstr = s[sliceindex:sliceindex+i]
                else:
                    data += str(datacount)
                    data += exstr
                    exstr = s[sliceindex:sliceindex+i]
                    datacount=1
                sliceindex+=i
        if datacount==1:
            data += s[sliceindex-i:]
        else:
            data += str(datacount)
            data += exstr
            data += s[sliceindex:]
        minval = min(minval, len(data))
    return minval

st = input()
print(solution(st))  