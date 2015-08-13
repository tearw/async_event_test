import sys

B = 'B'
W = 'W'
O = '0'
cellNum = 8

def getBoardFromFile(fileName):
    board = [([O] * cellNum) for i in range(cellNum)] 
    file = open(fileName,'r')
    
    x = 0
    y = 0
    for eachline in file:
        y = 0
        for character in eachline.strip():
            board[x][y] = character
            y += 1
        x += 1
    
    
    
    
    #for eachline in file:
    #    print(list(eachline.strip()))
    #    board.append(list(eachline.strip()))
    #file.close()
    #print('------------------')
    #print(board)
    return board
        
def outputBoardToFile(file, board):
    row = '--------\n'
    
    for x in range(cellNum):
        for y in range(cellNum):
            row += board[x][y]
        row += "\n"
    file.write(row)
    
def getBoardCopy(board):
    dupeBoard = [([O] * cellNum) for i in range(cellNum)] 

    for x in range(cellNum):
        for y in range(cellNum):
            dupeBoard[x][y] = board[x][y]

    return dupeBoard

def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != O or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile

    if tile == W:
        otherTile = B
    else:
        otherTile = W

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = O
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def isOnBoard(x, y):
    return x >= 0 and x <= cellNum - 1 and y >= 0 and y <= cellNum - 1


def getValidMoves(board, tile):
    validMoves = []

    for x in range(cellNum):
        for y in range(cellNum):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    print(xstart, ystart)
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True
    
if __name__ == '__main__':
    mainBoard = getBoardFromFile(sys.argv[1])
    outputFile = open(sys.argv[2],'w+')
    possibleMoves = getValidMoves(mainBoard, B)
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(mainBoard)
        makeMove(dupeBoard, B, x, y)
        #print(x, y)
        outputBoardToFile(outputFile, dupeBoard)
    outputFile.close()
                