def solution(k, room_number):
    room_dic = {}
    ret = []
    for request in room_number:
        n = request
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j]=n+1
    return ret