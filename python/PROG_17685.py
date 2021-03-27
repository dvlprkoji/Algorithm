import bisect

def countByRange(li, fr, to):
    return bisect.bisect_right(li,to)-bisect.bisect_left(li,fr)

def countPress(word, sortByLen):
    wordLen = len(word)
    for index in range(wordLen):
        fr, to = word[:index+1], word[:index+1]
        for i in range(maxlen-(index+1)):
            fr += 'a'
            to += 'z'
        res = 0
        for arrindex in countLen:
            if(arrindex>=index+1):
                res += countByRange(sortByLen[arrindex],fr[:arrindex],to[:arrindex])
        if res==1 : return index+1
    return wordLen
        
def solution(words):
    answer = 0
    global maxlen
    maxlen=0
    for word in words:
        maxlen = max(maxlen, len(word))
    sortByLen = [[] for _ in range(1000000)]
    global countLen
    countLen = set()
    for word in words:
        sortByLen[len(word)].append(word)
        countLen.add(len(word))
    for i in countLen:
        sortByLen[i].sort()
    for word in words:
        answer += countPress(word, sortByLen)
    return answer

words = ["go","gone","guild"]
print(solution(words))
