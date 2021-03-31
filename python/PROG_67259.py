def DFS(x, y, cost, exdir) :
    global minval
    if x==n-1 and y==n-2:
        if exdir==0:
            minval = min(minval, cost+600)
        else: 
            minval = min(minval, cost+100)
        return
    elif x==n-2 and y==n-1:
        if exdir==0: 
            minval = min(minval, cost+100)
        else: 
            minval = min(minval, cost+600)
        return
    for dir in range(4):
        mx = x + dx[dir]
        my = y + dy[dir]
        if mx<0 or my<0 or mx>=n or my>=n: continue
        if visited[mx][my]: continue
        if exdir==dir:
            if cost+100<minval:
                if minarr[mx][my][dir]>=cost+100:
                    minarr[mx][my][dir]=cost+100
                    visited[mx][my]=True
                    DFS(mx,my,cost+100,dir)
                    visited[mx][my]=False
        else:
            if cost+600<minval:
                if minarr[mx][my][dir]>=cost+600:
                    minarr[mx][my][dir]=cost+600
                    visited[mx][my]=True
                    DFS(mx,my,cost+600,dir)
                    visited[mx][my]=False

def solution(board):
    global b
    global visited, n
    global dx, dy
    global minval
    global minarr
    minval = 0x7f7f7f7f
    b = board
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    n = len(board)
    visited = [[False for i in range(n)] for j in range(n)]
    minarr = [[[0x7f7f7f7f for i in range(4)]for j in range(n)] for k in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]: visited[i][j]=True
    visited[0][0] = True
    if not board[0][1]:
        visited[0][1] = True
        DFS(0,1,100,1)
        visited[0][1] = False
    if not board[1][0]:
        visited[1][0] = True
        DFS(1,0,100,0)
    return minval

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))