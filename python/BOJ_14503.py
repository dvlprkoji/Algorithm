dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
x,y,d = map(int,input().split())

visited = [[False for i in range(m)]for j in range(n)]
board = []

for i in range(n):
    board.append(list(map(int,input().split())))


answer=0
done = False
visited[x][y]=True


while True:
    for dir in range(1,6):
        if dir==5:
            mx = x + dx[d-2]
            my = y + dy[d-2]
            if board[mx][my]==1:
                done=True
                break
            x,y = mx, my
            visited[mx][my]=True
            break
        mx = x + dx[d-dir]
        my = y + dy[d-dir]
        if mx<0 or my<0 or mx>=n or my>=m: continue
        if board[mx][my]==1: continue
        if visited[mx][my]: continue
        x,y = mx,my
        d = (d-dir)%4
        visited[x][y]=True
        break
    if done:
        for i in range(n):
            for j in range(m):
                if(visited[i][j]): answer+=1
        print(answer)
        break
        
