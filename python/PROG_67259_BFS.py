def BFS():
    global n, minval, board, dx, dy
    queue = []
    node = dict(x = 0, y = 0, ex = -1, cost = 0)
    queue.append(node)
    minval[0][0]=0
    while queue:
        cur = queue.pop(0)
        for dir in range(4):
            mx = cur["x"] + dx[dir]
            my = cur["y"] + dy[dir]
            if mx<0 or my<0 or mx>=n or my>=n: continue
            if b[mx][my] : continue
            if dir==cur["ex"] or cur["ex"]==-1: newcost = cur["cost"]+100
            else: newcost = cur["cost"]+600
            if minval[mx][my]<newcost: continue
            minval[mx][my]=newcost
            newnode = dict(x = mx,y = my, ex = dir, cost = newcost)
            queue.append(newnode)
    return minval[n-1][n-1]


def solution(board):
    global n, minval, b, dx, dy
    n = len(board)
    b=board
    minval = [[0x7f7f7f7f for i in range(n)]for j in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    return BFS()