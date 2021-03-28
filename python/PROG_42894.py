def removecheck(board, blocks):
    checklist = []
    if blocks[1][0] == blocks[2][0] and blocks[2][0] == blocks[3][0]:
        if blocks[0][1] == blocks[1][1]: 
            checklist.append((blocks[0][0],blocks[0][1]+1))
            checklist.append((blocks[0][0], blocks[0][1]+2))
        elif blocks[0][1] == blocks[2][1]:
            checklist.append((blocks[0][0],blocks[0][1]-1))
            checklist.append((blocks[0][0], blocks[0][1]+1))
        else:
            checklist.append((blocks[0][0],blocks[0][1]-2))
            checklist.append((blocks[0][0], blocks[0][1]-1))
    else:
        if blocks[1][1] == blocks[2][1]:
            checklist.append((blocks[3][0]-1, blocks[3][1]))
        else: 
            checklist.append((blocks[2][0]-1, blocks[2][1]))
    for block in checklist:
        possible = True
        for x in range(0,block[0]+1):
            if board[x][block[1]] != 0:
                possible=False
                break
        if not possible: return False
    return True

def typecheck(blocks):
    if blocks[0][0]==blocks[1][0]: return False
    if blocks[1][0]==blocks[2][0] and blocks[2][0]!=blocks[3][0]: return False
    return True

def solution(board):
    answer = 0
    candidate = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=0:
                if board[i][j] not in  candidate: candidate[board[i][j]]=[]
                candidate[board[i][j]].append((i,j))
    removelist = []
    for blocks in candidate:
        if not typecheck(candidate[blocks]):
            removelist.append(blocks)
    for  i in removelist:
        del candidate[i]
    while True:
        done = True
        for blocks in candidate:
            if removecheck(board, candidate[blocks]): 
                done = False
                answer += 1
                break
        if done: break
        else: 
            for block in candidate[blocks]:
                board[block[0]][block[1]] = 0
            del candidate[blocks]
    return answer