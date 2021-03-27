import datetime

pushTime = []
popTime = []


def check(t):
    st = t-datetime.timedelta(microseconds=999000)
    en = t
    res = 0
    for i in range(len(lines)):
        if st>popTime[i] or en<pushTime[i]: continue
        res += 1
    return res


def solution(lines):
    answer = 0

    for line in lines:
        day = datetime.date.fromisoformat(line.split()[0])
        time = datetime.time.fromisoformat(line.split()[1])
        delay = datetime.timedelta(microseconds=int(float(line.split()[2].replace('s',''))*1000-1)*1000)
        dateTime = datetime.datetime.combine(day,time)
        popTime.append(dateTime)
        dateTime = dateTime-delay
        pushTime.append(dateTime)

    for i in range(len(pushTime)):
        answer = max(answer, check(pushTime[i]))
        answer = max(answer, check(popTime[i]))

    return answer
