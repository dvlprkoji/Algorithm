def solution(board, moves):
    n = len(board)
    answer=0
    top = []
    for y in range(n):
        count = -1
        for x in range(n):
            if board[x][y]!=0:
                count=x
                break
        if count==-1: top.append(5)
        else: top.append(count)

    basket = []
    for move in moves:
        move-=1
        if top[move]<n: val = board[top[move]][move]
        else: continue
        top[move]+=1
        if basket and basket[len(basket)-1] == val:
            basket.pop()
            answer+=2
        else:
            basket.append(val)
    
    return answer
