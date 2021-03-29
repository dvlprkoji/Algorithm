import bisect

def countByRange(li, fr, to):
    return bisect.bisect_right(li,to) - bisect.bisect_left(li,fr)

def solution(words, queries):
    answer = []
    wordList = {}
    revList = {}        
    for word in words:
        if len(word) not in wordList: wordList[len(word)] = []
        if len(word) not in revList: revList[len(word)] = []
        wordList[len(word)].append(word)
        revList[len(word)].append(word[::-1])
    for leng in wordList:
        wordList[leng].sort()
        revList[leng].sort()
    for query in queries:
        if query[0] == '?':
            fr = query[::-1].replace('?','a')
            to = query[::-1].replace('?','z')
            if len(query) in wordList:
                answer.append(countByRange(revList[len(query)],fr,to))
            else: answer.append(0)
        else:
            fr = query.replace('?','a')
            to = query.replace('?','z')
            if len(query) in wordList:
                answer.append(countByRange(wordList[len(query)],fr,to))
            else: answer.append(0)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))